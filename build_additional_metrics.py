import csv,pathlib,re
p=pathlib.Path(__file__).parent
schema=list(csv.DictReader(open(p/'evidence/metadata-before.csv')))
rows=[]
def add(n,t,e,d):
 cols={r['Column Name'] for r in schema if r['Table Name']==t and r['Column Name']};full='wisdomai.'+t
 e=re.sub(r'\b[a-z][a-z_0-9]*\b',lambda m:full+'.'+m.group() if m.group() in cols else m.group(),e)
 rows.append([n,d,e,'wisdomai','SQL','TABLE','Ali-TD',full,e,e,'DISPLAY_FORMAT_UNKNOWN',2,'true',''])
for n,t,e,d in [
('Cabin Passenger Count Load Factor %','FLIGHT_CABIN_LOAD','100.0*SUM(passengers_boarded)/NULLIF(SUM(seats_available),0)','Boarded passengers / available cabin seats; ratio of sums at flight-cabin grain.'),
('Cabin Passenger Revenue','FLIGHT_CABIN_LOAD','SUM(passenger_revenue)','Passenger revenue at flight-cabin grain in source units.'),
('Service Case Count','SERVICE_CASE','COUNT(service_case_key)','Count of service cases, not unique passengers.'),
('First Contact Resolution %','SERVICE_CASE','100.0*SUM(CASE WHEN first_contact_resolved_flag=1 THEN 1 ELSE 0 END)/NULLIF(SUM(CASE WHEN first_contact_resolved_flag IN (0,1) THEN 1 ELSE 0 END),0)','Share of valid binary first-contact-resolution flags equal to 1.'),
('Average Service Resolution Days','SERVICE_CASE','AVG(resolution_days)','Mean recorded non-null resolution days; open cases may have no recorded resolution.'),
('Average Service CSAT','SERVICE_CASE','AVG(csat_score)','Mean non-null service-case satisfaction score; preserve recorded score scale.'),
('Baggage Claim Count','BAGGAGE_CLAIM','COUNT(baggage_claim_key)','Claim records, not number of bags or unique passengers.'),
('Baggage Compensation','BAGGAGE_CLAIM','SUM(compensation_amount)','Recorded baggage compensation in source monetary units.'),
('Baggage Average Resolution Days','BAGGAGE_CLAIM','AVG(days_to_resolve)','Mean non-null recorded days to resolve a baggage claim.'),
('Maintenance Event Cost','MAINTENANCE_EVENT','SUM(total_cost)','Total recorded cost at maintenance-event grain.'),
('Maintenance Downtime Hours','MAINTENANCE_EVENT','SUM(downtime_hours)','Recorded event downtime hours. Overlapping events can overlap elapsed aircraft downtime; do not call this distinct aircraft out-of-service duration.'),
('Crew Overtime Hours','CREW_ASSIGNMENT','SUM(overtime_minutes)/60.0','Assignment overtime minutes converted to hours; not unique flight duration.'),
('Crew Assignment Pay','CREW_ASSIGNMENT','SUM(crew_pay)','Recorded pay at crew-assignment grain; do not add to route crew cost without reconciliation.'),
('Card Application Approval %','CARD_APPLICATION','100.0*SUM(CASE WHEN approved_flag=1 THEN 1 ELSE 0 END)/NULLIF(COUNT(*),0)','Approved application records divided by all application records; not approval among decided-only applications.'),
('Cardholder Spend','CARD_ACCOUNT_MONTHLY','SUM(total_spend)','Recorded account-month card spend; not airline revenue.'),
('Loyalty Miles Earned','LOYALTY_MONTHLY','SUM(miles_earned_total)','Monthly loyalty miles earned; additive flow, unlike miles_balance_end.'),
('Loyalty Miles Redeemed','LOYALTY_MONTHLY','SUM(miles_redeemed)','Monthly loyalty miles redeemed; additive flow.'),
('Survey Response Count','PASSENGER_SURVEY','COUNT(survey_key)','Survey records; include valid NPS denominator separately when computing NPS.'),
('Average Airport Weather Severity','AIRPORT_DAY_WEATHER','AVG(weather_severity_score)','Mean recorded severity at airport-day grain; not flight-weighted and not a causal estimate.'),
('Ancillary Transaction Count','ANCILLARY_SALE','COUNT(ancillary_sale_key)','Ancillary sale records, not passengers or total item quantity.')]:add(n,'ZAL_VW_'+t,e,d)
h=['Name','Description','SQL','Database','Type','Scope','Connection','Tables','Expression','Expanded SQL','Display Format','Precision','Included','Stale Reason']
for f in [p/'context/additional-metrics.csv',pathlib.Path('/private/tmp/td-airline-additional-metrics.csv')]:
 with f.open('w') as o:w=csv.writer(o);w.writerow(h);w.writerows(rows)
print(len(rows),'additional metrics')
