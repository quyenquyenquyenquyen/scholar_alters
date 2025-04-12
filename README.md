# Scholar Alters
Parse unread emails from Google Scholar alerts and update README.md.

## Setting for First Use
1. Use the [Gmail API Client Library](https://developers.google.com/gmail/api/quickstart/python) and create a `credentials.json` file as explained in the link.

    Example structure:
    ```
    .
    ├── credentials.json
    ```

    Example `credentials.json`:
    ```json
    {
         "installed": {
              "client_id": "YOUR_CLIENT_ID",
              "project_id": "YOUR_PROJECT_ID",
              "auth_uri": "https://accounts.google.com/o/oauth2/auth",
              "token_uri": "https://oauth2.googleapis.com/token",
              "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
              "client_secret": "YOUR_CLIENT_SECRET",
              "redirect_uris": [
                    "http://localhost"
              ]
         }
    }
    ```

2. Run `script.sh`:
    ```
    bash script.sh
    ```
    For the first run, you will need to log in to your Google account. Ensure that your Gmail account is added as a test user for your app. Refer to this [Stack Overflow post](https://stackoverflow.com/questions/75454425/access-blocked-project-has-not-completed-the-google-verification-process) for guidance.

    This will create a `./data/token.json` file.

3. Copy the information from `token.json` into a GitHub Action secret variable named `TOKEN_CONFIG_JSON`.

    Example `token.json`:
    ```json
    {
         "token": "YOUR_ACCESS_TOKEN",
         "refresh_token": "YOUR_REFRESH_TOKEN",
         "token_uri": "https://oauth2.googleapis.com/token",
         "client_id": "YOUR_CLIENT_ID",
         "client_secret": "YOUR_CLIENT_SECRET",
         "scopes": [
              "https://mail.google.com/",
              "https://www.googleapis.com/auth/gmail.readonly"
         ],
         "universe_domain": "googleapis.com",
         "account": "",
         "expiry": "YOUR_EXPIRY_DATE"
    }
    ```

## Run
Run the following command from your CLI:
```
bash script.sh
```

## Papers

| Topic | Branch | Papers |
| --- | --- | --- |
| Code | Search | [MGS3: A Multi-Granularity Self-Supervised Code Search Framework](https://scholar.google.com/scholar_url?url=https://dl.acm.org/doi/abs/10.1145/3690624.3709263&hl=en&sa=X&d=1009890518697704121&ei=FX75Z5i1FrGyieoPw4eO4A4&scisig=AFWwaebymtIN-0ZFuPvqxNkkLlXu&oi=scholaralrt&hist=ylyK0_8AAAAJ:16898579961534012346:AFWwaeZADCuvrSiGaZ1pge7b9bMB&html=&pos=0&folt=rel) |
| LLM, Code |  | [Evaluating the Generalization Capabilities of Large Language Models on Code Reasoning](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.05518&hl=en&sa=X&d=805905684378306330&ei=FX75Z5i1FrGyieoPw4eO4A4&scisig=AFWwaeZ9BtEhgM_L83-1uaig0DXh&oi=scholaralrt&hist=ylyK0_8AAAAJ:16898579961534012346:AFWwaeZADCuvrSiGaZ1pge7b9bMB&html=&pos=1&folt=rel) |
| Vulnerabilities, LLM | Detection | [Reasoning with LLMs for Zero-Shot Vulnerability Detection](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.17885&hl=en&sa=X&d=16151102993317123730&ei=FX75Z_e_DsmpieoPv7aWiQ4&scisig=AFWwaeaU1duZG60YHiU0D1fyotku&oi=scholaralrt&hist=ylyK0_8AAAAJ:4812769200119993430:AFWwaeYwgMeQSPpxCfDXmGy5aE3n&html=&pos=0&folt=rel) |
| LLM, Code | Generation | [A Comprehensive Study of LLM Secure Code Generation](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.15554%3F&hl=en&sa=X&d=1363137439941333778&ei=FX75Z_e_DsmpieoPv7aWiQ4&scisig=AFWwaea70lzbx-2dnx-SlddbyIDc&oi=scholaralrt&hist=ylyK0_8AAAAJ:4812769200119993430:AFWwaeYwgMeQSPpxCfDXmGy5aE3n&html=&pos=1&folt=rel) |
|  | Generation | [Retrieval-Augmented Fine-Tuning for Improving Retrieve-and-Edit Based Assertion Generation](https://scholar.google.com/scholar_url?url=https://ieeexplore.ieee.org/abstract/document/10949862/&hl=en&sa=X&d=1832626827113407670&ei=FX75Z5P9EsCSieoPgfq5yAo&scisig=AFWwaeYd1ZjQg27v5i1h4-T0_o0S&oi=scholaralrt&hist=ylyK0_8AAAAJ:15035864585353249078:AFWwaeZamHljvPChNBtOABcetGTp&html=&pos=0&folt=cit) |
|  |  | [SoK: Frontier AI's Impact on the Cybersecurity Landscape](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.05408&hl=en&sa=X&d=8797189251482550811&ei=FX75Z5P9EsCSieoPgfq5yAo&scisig=AFWwaeaiUdJD8sWdAsXbQZqsuu0D&oi=scholaralrt&hist=ylyK0_8AAAAJ:15035864585353249078:AFWwaeZamHljvPChNBtOABcetGTp&html=&pos=1&folt=cit) |
| LLM, Code | Generation | [Enhancing High-Quality Code Generation in Large Language Models with Comparative Prefix-Tuning](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.09020&hl=en&sa=X&d=274986171076802173&ei=FX75Z5vwF8uZieoPg4fsmAg&scisig=AFWwaea-q7yfbqCfb2mRj_yZrJ7q&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=1&folt=rel) |
| LLM, Code | Generation | [Fixing Large Language Models' Specification Misunderstanding for Better Code Generation](https://scholar.google.com/scholar_url?url=https://drive.google.com/file/d/1eiTmCxYs6FgdxCZNOdS9egz6U1Jf4wOL/view&hl=en&sa=X&d=6513233471596826292&ei=FX75Z5vwF8uZieoPg4fsmAg&scisig=AFWwaeZjNzZZqbOuWO8MZmi5NgiS&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=2&folt=rel) |
|  |  | [Exploring the Lifecycle and Maintenance Practices of Pre-Trained Models in Open-Source Software Repositories](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.06040&hl=en&sa=X&d=5791951061414034500&ei=FX75Z5vwF8uZieoPg4fsmAg&scisig=AFWwaearbzhUesD4E-PQqPp1R7rY&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=3&folt=rel) |
| Vulnerabilities, LLM | Exploit | [HALURust: Exploiting Hallucinations of Large Language Models to Detect Vulnerabilities in Rust](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.10793&hl=en&sa=X&d=5829414047755650757&ei=FX75Z5vwF8uZieoPg4fsmAg&scisig=AFWwaeY9qSDL2ktzIVFeZhrU-G2d&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=4&folt=rel) |
| Software Testing | Generation | [KotSuite: Unit Test Generation for Kotlin Programs in Android Applications](https://scholar.google.com/scholar_url?url=https://qixin5.github.io/files/pdf/research/icpc25kotsuite.pdf&hl=en&sa=X&d=4160603672644182246&ei=FX75Z5vwF8uZieoPg4fsmAg&scisig=AFWwaebk9skrRKkb80KaNdrfD3RV&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=5&folt=rel) |
| Fuzzing |  | [Fuzzing: On Benchmarking Outcome as a Function of Benchmark Properties](https://scholar.google.com/scholar_url?url=https://dylanjwolff.com/assets/eval.pdf&hl=en&sa=X&d=3899393433676860100&ei=FX75Z5vwF8uZieoPg4fsmAg&scisig=AFWwaeZCpAIF5IaVvnEXyVRhuvNd&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=6&folt=rel) |
| Vulnerabilities, LLM | Detection | [Evaluating Biased Synthetic Data Effects on Large Language Model-Based Software Vulnerability Detection](https://scholar.google.com/scholar_url?url=https://www.scitepress.org/Papers/2025/131568/131568.pdf&hl=en&sa=X&d=2607917738470903508&ei=FX75Z5vwF8uZieoPg4fsmAg&scisig=AFWwaeZ0Q2EahjIXC8AC_4u3u9GS&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=8&folt=rel) |
| Commit Message | Generation | [Dataset collection for automatic generation of commit messages](https://scholar.google.com/scholar_url?url=https://www.rtj-mirea.ru/jour/issue/download/57/76%23page%3D8&hl=en&sa=X&d=11738522829282307678&ei=FX75Z5vwF8uZieoPg4fsmAg&scisig=AFWwaeZ3_DGZkQ2HI7j6l3KtFhuh&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=9&folt=rel) |
| Code | Generation | [Modularization is Better: Effective Code Generation with Modular Prompting](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.12483&hl=en&sa=X&d=14254932694001679206&ei=FX75Z9mTEJm7ieoP3oH9uAU&scisig=AFWwaebJFNOBSO1Oa5RjObIyQw5e&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=3&folt=rel) |
| Vulnerabilities | Detection | [How Do Solidity Versions Affect Vulnerability Detection Tools? An Empirical Study](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.05515&hl=en&sa=X&d=10406177812794992313&ei=FX75Z9mTEJm7ieoP3oH9uAU&scisig=AFWwaeYkpOtMh71pWOgA4odw8ZlC&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=5&folt=rel) |
| LLM, Software Testing |  | [LLM-assisted Mutation for Whitebox API Testing](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.05738&hl=en&sa=X&d=7557048715145801310&ei=FX75Z9mTEJm7ieoP3oH9uAU&scisig=AFWwaeZ-CTfa-2rzX0xbP2wE_SKz&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=6&folt=rel) |
|  |  | [CBPF: A Novel Method For Filtering Poisoned Data Based on Composite Backdoor Attacks](https://scholar.google.com/scholar_url?url=https://ieeexplore.ieee.org/abstract/document/10954977/&hl=en&sa=X&d=14956579577820071145&ei=FX75Z8jEFNSyieoP2ane-QQ&scisig=AFWwaeYcJx9MusTKHvt-hle13r9Q&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=0&folt=rel) |
|  |  | [Defending Deep Neural Networks against Backdoor Attacks via Module Switching](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.05902&hl=en&sa=X&d=8952997710940951785&ei=FX75Z8jEFNSyieoP2ane-QQ&scisig=AFWwaebMnBVDpo1_qCHfNg_gyeFe&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=1&folt=rel) |
| LLM, Code | Generation | [LLMs Meet Library Evolution: Evaluating Deprecated API Usage in LLM-based Code Completion](https://scholar.google.com/scholar_url?url=https://www.computer.org/csdl/proceedings-article/icse/2025/056900a781/251mHK5tjdC&hl=en&sa=X&d=4291983748355056793&ei=FX75Z8jEFNSyieoP2ane-QQ&scisig=AFWwaebbFgNB42GTnyK8DsY5wt9u&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=2&folt=rel) |
| LLM | Agent | [Bridging Industrial Expertise and XR with LLM-Powered Conversational Agents](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.05527&hl=en&sa=X&d=665950199627025975&ei=FX75Z8jEFNSyieoP2ane-QQ&scisig=AFWwaebU2ZAPYX5DEiQ9lYaxtIxy&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=3&folt=rel) |
|  |  | [Evolution-based Region Adversarial Prompt Learning for Robustness Enhancement in Vision-Language Models](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.12874&hl=en&sa=X&d=4288320110718600484&ei=FX75Z8jEFNSyieoP2ane-QQ&scisig=AFWwaebZ47dtXpHPS7gkzptvLmTz&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=4&folt=rel) |
| LLM |  | [XSShield: Defending Against Stored XSS Attacks Using LLM-Based Semantic Understanding](https://scholar.google.com/scholar_url?url=https://www.mdpi.com/2076-3417/15/6/3348&hl=en&sa=X&d=11849643047241211005&ei=FX75Z8jEFNSyieoP2ane-QQ&scisig=AFWwaeZJp-xCesiNk9t9IXhXxSLJ&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=5&folt=rel) |
| Vulnerabilities, Verification, LLM | Detection | [Vulnerability Detection: From Formal Verification to Large Language Models and Hybrid Approaches: A Comprehensive Overview](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.10784&hl=en&sa=X&d=12911561823202945144&ei=FX75Z8jEFNSyieoP2ane-QQ&scisig=AFWwaeYhatByJp-efqzH8QuYSI72&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=6&folt=rel) |
|  | Agent | [AgentDAM: Privacy Leakage Evaluation for Autonomous Web Agents](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.09780%3F&hl=en&sa=X&d=12860650719968363446&ei=FX75Z8jEFNSyieoP2ane-QQ&scisig=AFWwaeaZP1nOXGDyZqifdZ_WOtaf&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=7&folt=rel) |
| LLM |  | [Dapo: An open-source llm reinforcement learning system at scale](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.14476&hl=en&sa=X&d=1968980266662184520&ei=FX75Z8jEFNSyieoP2ane-QQ&scisig=AFWwaebXNS6d8Y_C8FG4sfvmXe0u&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=8&folt=rel) |
| LLM | Generation | [Sugar-Coated Poison: Benign Generation Unlocks LLM Jailbreaking](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.05652&hl=en&sa=X&d=9735385300123201340&ei=FX75Z8jEFNSyieoP2ane-QQ&scisig=AFWwaeYrOPjdrzg0rfaML-0wq6dO&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=9&folt=rel) |
| Bug |  | [CAI: An Open, Bug Bounty-Ready Cybersecurity AI](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.06017&hl=en&sa=X&d=17999546665399519711&ei=FX75Z_eLDYSlieoPpZSOmAc&scisig=AFWwaeYPU6hfAgxSLSQhxSdg3yiu&oi=scholaralrt&hist=ylyK0_8AAAAJ:4436498698466669065:AFWwaebib5Pw9QKWi9BJ6ThKDwc5&html=&pos=1&folt=cit) |
