"""Offline integrity checks for the reusable workshop kit; no credentials/network."""
import csv, json, pathlib, re
ROOT = pathlib.Path(__file__).parent

def rows(path):
    with open(ROOT / path, newline='') as f:
        reader = csv.DictReader(f)
        assert reader.fieldnames and len(reader.fieldnames) == len(set(reader.fieldnames)), path
        data = list(reader)
        assert all(None not in row for row in data), f'Ragged CSV: {path}'
        return data

schema = {t['name']: {c['name'] for c in t['columns']} for t in json.loads((ROOT/'context/schema-reference.json').read_text())}
for path in ROOT.rglob('*.csv'):
    rows(path.relative_to(ROOT))
metrics = rows('context/metrics-complete.csv')
assert len(metrics) == 43 and len({r['Name'] for r in metrics}) == 43
for metric in metrics:
    assert not metric['Stale Reason'], metric['Name']
    for table, col in re.findall(r'wisdomai\.(ZAL_\w+)\.(\w+)', metric['SQL']):
        assert col in schema[table], (metric['Name'], table, col)
relationships = rows('context/relationships.csv')
assert len(relationships) == 49
for r in relationships:
    assert r['Source Column'] in schema[r['Source Table']], r
    assert r['Destination Column'] in schema[r['Destination Table']], r
for r in rows('context/entities.csv'):
    for field in ('ID Column', 'Name Column'):
        table, col = r[field].split('.')
        assert col in schema[table], r
assert len(rows('context/entities.csv')) == 11
assert len(rows('context/knowledge.csv')) == 23
assert len(rows('context/synonyms.csv')) == 23
assert len(rows('skills/skills-import.csv')) == 6
assert all('---' in r['Skill Markdown'] for r in rows('skills/skills-import.csv'))
reviewed = rows('context/reviewed-queries.csv')
assert len(reviewed) == 31
training = rows('training/candidate_queries.csv')
assert len(training) == 30
assert all(r['Query'] in {q['Query'] for q in reviewed} for r in training)
for path, count in [('evaluations/holdout-import.csv', 16), ('evaluations/numeric-storage-import.csv', 5)]:
    cases = rows(path)
    assert len(cases) == count
    for case in cases:
        assert isinstance(json.loads(case['assertions']), list)
notes = rows('storage/WORKSHOP_SYNTHETIC_service_notes.csv')
assert len(notes) == 8 and len({r['note_id'] for r in notes}) == 8
assert all(r['synthetic_flag'] == '1' for r in notes)
assert {r['note_id'] for r in notes if r['scenario']=='baggage'} == {'SYN-002','SYN-007'}
# Training and semantic holdout wording must be separate.
assert not {r['Query'].strip().lower() for r in training} & {r['query'].strip().lower() for r in rows('evaluations/holdout-import.csv')}
print('PASS: CSV structures, 43 metric references, 49 relationships, 11 entities, 30 reviewed training questions, evaluation inputs and synthetic IDs.')
print('Live execution and behavioral validation are recorded separately under evidence/.')
