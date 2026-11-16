# WisdomAI workshop glossary

Plain-language definitions for the three-hour workshop. Use these alongside [the student workbook](WORKSHOP_LABS.md). This glossary incorporates the working draft developed during the facilitator walkthrough; we will refine it as the class materials are tested.

## 1. Domains and data meaning

| Term | Definition you can say aloud | Airline example |
| --- | --- | --- |
| Domain | A workspace that brings selected data together with the context needed to interpret and answer questions about a subject. | CSA Workshop - Facilitator |
| Connection | Configuration allowing WisdomAI to access a source system using an approved identity and access scope. | The provisioned Teradata connection; credentials are not in this repository. |
| Data source | A place a domain gets information from, such as a database or storage. | Airline data in Teradata; Tera Storage |
| Schema | The structure and names of data objects and columns. Depending on the database, “schema” can also mean a named namespace. | Flight and survey objects and their fields |
| Metadata | Descriptions and properties that explain data structure, names and intended use. | A description saying flight_date represents the travel date |
| Table | Structured information organized into rows and columns. | One synthetic service note per row |
| View | A named query that presents data as a table-like result. Do not assume it is a separate copy of the underlying business facts. | ZAL_VW_FLIGHT enriches flight facts with descriptive fields. |
| Grain | What exactly one row represents. | One flight leg, one survey response, or one route-month |
| Primary key | A column, or combination of columns, that uniquely identifies a row. Check uniqueness and missing values before declaring it a key. | flight_key identifies a flight leg. |
| Composite key / grain | Two or more attributes are needed together to identify the row's level of detail. | A route repeats each month; route plus month identifies a route-month. |
| Relationship | A declared way that records in two objects match through keys. | Many flight rows can refer to one route. |
| Cardinality | How many records can match across a relationship: One to One, Many to One, One to Many, or Many to Many. | Flights to route is Many to One when the route key is unique in the route object. |
| Fanout | A join multiplies rows, potentially counting a measure more than once. | Joining multiple surveys and ticket rows before summing route revenue |
| Event-date basis | The date used to decide which reporting period a record belongs to. | Booking date and flight date answer different questions. |

## 2. Business context and analytical behavior

| Term | Definition you can say aloud | Airline example |
| --- | --- | --- |
| Business context | Definitions, conventions and rules needed to interpret data correctly. | Which date to use, what a measure means, and which records qualify |
| Knowledge | Written business context that guides interpretation and analysis. | Use historical month-end tier for historical loyalty segmentation. |
| Synonym | An alternative name or phrase for the same concept. It does not define the calculation. | NPS and Net Promoter Score |
| Metric | A named business calculation with its definition, source, units and relevant eligibility rules. | Operating margin or NPS |
| Entity | An identifiable business object with an ID and a useful display name, allowing questions to refer to that object consistently. | Route ID and route code; aircraft ID and tail number |
| Skill | A reusable analytical procedure for a type of question. It describes what steps to follow. | Resolve period, select route-month financials, calculate measures, compare with budget, state limitations. |
| Prompt | The question or instruction supplied to the assistant. Its wording supplies immediate task context. | “Review September 2026 route profitability against budget.” |
| SQL | A language for querying structured data. Executable SQL can still express the wrong business question. | Filter September flight dates, then count flights by route. |

A useful teaching distinction: **a synonym identifies the concept; a metric defines the calculation; knowledge explains its interpretation; a skill defines the analytical steps.** These complement each other.

## 3. Calculations and populations

| Term | Definition you can say aloud | Airline example |
| --- | --- | --- |
| Filter | A condition deciding which rows are included. A flag does not independently prove that its label is true. | WHERE synthetic_flag = 1 |
| Aggregation | Combining multiple rows into a summary using operations such as COUNT, SUM or AVG. | Count notes grouped by scenario. |
| Numerator | The value above the division line. | Operating income |
| Denominator | The value below the division line: the total or eligible population used for comparison. | Total revenue; valid survey response count |
| Ratio of sums | Add each relevant measure over the selected records, then divide the totals. | SUM(operating_income) / SUM(total_revenue), rather than an unweighted average of route margins |
| Snapshot measure | A value describing a state at a particular time; adding it across periods can count the same balance repeatedly. | miles_balance_end at a chosen month end |
| Flow measure | An activity amount occurring during a period, which can often be added over non-overlapping periods with compatible definitions. | Miles earned during a month |
| Null / undefined | A missing or undefined value, distinct from zero. | A ratio with no valid denominator is undefined. |
| NPS | Percentage of promoters (scores 9–10) minus percentage of detractors (0–6). Passives (7–8) remain in the valid 0–10 denominator. Range −100 to +100. | 60% promoters minus 20% detractors gives NPS 40, not a mean rating of 40. |
| Operating margin | Operating income divided by revenue, multiplied by 100. It can be negative when there is a loss. | 20 income / 100 revenue × 100 = 20% |

## 4. Training, review and evaluation

| Term | Definition you can say aloud | Workshop example |
| --- | --- | --- |
| Training example / training set | Example questions and any guidance used to generate and inspect candidate answers or SQL and establish expected domain behavior. This is not retraining the underlying language model. | One question about September flights by route, with reference SQL guidance |
| Candidate match | A proposed answer or SQL query for an example question that still needs inspection. | Generated SQL awaiting a review decision |
| Reviewed query | A question/SQL example retained after a review/approval decision. Its reliability depends on the checks performed and whether sources or definitions have changed. | September route income SQL checked against the source |
| Evaluation set | A collection of test questions with expected results or behaviors used to assess answers and detect problems. | Three cases testing numbers, ambiguity handling and a held-out question |
| Test case | One question, its relevant scope, and what would count as correct behavior or output. | “Convert revenue to euros” should ask for missing currency/FX basis. |
| Assertion | A specific condition used to check an answer. | Answer states the survey-date basis and includes valid response counts. |
| Ground truth | A reference result used for comparison, established independently rather than copied uncritically from the answer being tested. It must itself be validated. | Results from an independently checked source SQL query |
| Holdout | Test examples kept apart from the examples used during setup/training to assess behavior beyond those examples. | An untrained period, grouping or phrasing with defined expectations |
| Judge | The mechanism assessing an answer against expectations. A judge can make mistakes; inspect its reasoning and the source evidence. | An evaluation explanation classifying a response as passing or failing |
| Pass rate | Passed scored cases divided by scored cases for the stated run and conditions. It is not a universal product accuracy guarantee. | Three passes out of three cases in one recorded mode/run |
| Regression | A previously working behavior becomes worse after a change. | A context edit makes a date-sensitive answer use the wrong month basis. |
| Validation | Checking that a result and its method satisfy the intended business meaning and source evidence. | Correct source, grain, period, denominator, units, and reconciliation |

**Training helps establish examples; review decides what to accept; evaluation tests whether expected behavior holds.** Keep the activities and evidence distinct.

## 5. Storage and retrieved evidence

| Term | Definition you can say aloud | Workshop example |
| --- | --- | --- |
| Tera Storage | The storage label observed in the Teradata-branded instance. Display names can differ from physical SQL names. | SQL may still use wisdom_storage. |
| Derived column | A row-level calculation added to a table-like object. | A synthetic-data classification label for each note |
| Derived table | A table-like object defined by a query over existing data, often to reshape or summarize it. The term alone does not establish whether results are physically stored or recomputed. | One row per scenario with a count of synthetic notes |
| File | An uploaded document whose processed contents can supply information for answers. Upload, processing and successful retrieval are separate checkpoints. | WORKSHOP_SYNTHETIC_facilitator_brief.txt |
| Retrieval / RAG | Finding relevant source information and using it to support a generated answer. RAG means retrieval-augmented generation. | Retrieve baggage notes or a passage from the facilitator brief. |
| Citation | A reference to source material supporting an answer. Check that the cited text actually supports the claim. | SYN-002, SYN-007, or the facilitator brief |
| Synthetic data | Invented teaching or testing material, clearly distinguished from actual business evidence. | The eight workshop service narratives |

## 6. Presenting and reproducing results

| Term | Definition you can say aloud | Workshop example |
| --- | --- | --- |
| LiveApp | An interactive application experience built around a use case. It can help present and explore information; the domain and source checks still matter. | Passenger Experience Scorecard in the Teradata environment |
| Reproducibility | Another person can repeat the stated process and check its result using the specified inputs, sources and scope. | A handoff includes the prompt, domain, period, source, checked result and limitations. |
| Provenance | Where information came from and how it was produced or transformed. | A note is invented workshop content; a summary counts those notes. |

This glossary is for learning and explanation. For exact controls in the assigned instance, follow the workbook and the instructor's live demonstration.
