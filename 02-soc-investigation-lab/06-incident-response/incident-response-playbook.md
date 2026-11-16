\# Incident Response Playbook – Suspicious Authentication Activity



\## 1. Purpose



This playbook documents a structured response to suspicious authentication activity identified during the SOC Investigation Lab.



The scenario is simulated and intended for educational and portfolio purposes.



\## 2. Simulated Incident Summary



\*\*Incident type:\*\* Suspected brute-force authentication activity  

\*\*Affected account:\*\* `jdoe`  

\*\*Source IP:\*\* `203.0.113.45`  

\*\*Target system:\*\* `WORKSTATION-01`  

\*\*Severity:\*\* High – preliminary assessment



The investigation identified five consecutive failed login attempts followed by a successful login from the same source IP.



This pattern may indicate a compromised account, but the available logs alone do not confirm unauthorized access.



\## 3. Incident Response Steps



\### Step 1: Identification



\- Review authentication logs for repeated failed login attempts.

\- Identify affected usernames, source IP addresses, timestamps, and destination systems.

\- Check whether a successful login followed the failed attempts.

\- Review related alerts and historical authentication activity.



\### Step 2: Initial Analysis



\- Determine the number and timing of failed attempts.

\- Compare the source IP associated with failed and successful logins.

\- Check whether the affected account has privileged access.

\- Review available evidence for unusual login locations or activity.



\### Step 3: Containment



If the activity is confirmed as unauthorized, and in accordance with organizational procedures:



\- Escalate the incident to the appropriate security team.

\- Request temporary account disablement or session revocation through authorized administrators.

\- Consider blocking the suspicious source IP where appropriate.

\- Preserve relevant authentication logs and investigation evidence.



\### Step 4: Eradication



After confirming account compromise:



\- Reset the affected account's credentials.

\- Revoke active sessions and review authentication tokens.

\- Check for unauthorized account changes or persistence mechanisms.

\- Review endpoint and identity logs for additional suspicious activity.



\### Step 5: Recovery



\- Restore account access only after security checks are completed.

\- Require multi-factor authentication where supported.

\- Monitor subsequent login activity.

\- Confirm that affected systems and accounts are operating normally.



\### Step 6: Lessons Learned



\- Review whether existing detection rules identified the activity effectively.

\- Identify opportunities to improve authentication monitoring.

\- Document investigation findings and response actions.

\- Recommend improvements to account security and alerting procedures.



\## 4. Evidence to Preserve



\- Original authentication log records.

\- Detection script output.

\- Relevant Splunk search results and dashboard screenshots.

\- Investigation notes and timestamps.

\- Incident escalation and response records, if applicable.



\## 5. MITRE ATT\&CK Mapping



\- \*\*T1110 – Brute Force:\*\* Repeated failed authentication attempts.

\- \*\*T1078 – Valid Accounts:\*\* Successful authentication following repeated failures may warrant investigation for possible account misuse.



These mappings describe potential techniques, not confirmed attacker activity.



\## 6. Important Limitations



\- The dataset contains synthetic authentication events.

\- No real account or system was accessed or compromised.

\- No containment, eradication, or recovery actions were performed.

\- Response actions are proposed procedures, not completed operational actions.

\- The source IP addresses are reserved documentation addresses.



\## 7. Conclusion



This playbook demonstrates a structured approach to identifying, investigating, containing, and recovering from suspicious authentication activity. It provides a documented incident response workflow for the simulated SOC investigation scenario.

