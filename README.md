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

| Topic | Branch | Papers | Related to |
| --- | --- | --- | --- |
| LLM |  | [ELAB: Extensive LLM Alignment Benchmark in Persian Language](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.12553&hl=en&sa=X&d=4417832566291085341&ei=Dl8FaMQDiKjqtA-e-tPxDg&scisig=AFWwaeZpv_cWtEy5wRhj9-GUvaCL&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=0&folt=rel) | Richard Fang |
| Vulnerabilities, LLM, Code | Detection, Agent | [LLM Agentic Workflow for Automated Vulnerability Detection and Remediation in Infrastructure-as-Code](https://scholar.google.com/scholar_url?url=https://ieeexplore.ieee.org/iel8/6287639/6514899/10965635.pdf&hl=en&sa=X&d=14219617279893468661&ei=Dl8FaMQDiKjqtA-e-tPxDg&scisig=AFWwaeY0OWR9oTONDgJw1vBZERtQ&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=1&folt=rel) | Richard Fang |
| Vulnerabilities, Smart Contracts, LLM | Detection | [MOS: Towards Effective Smart Contract Vulnerability Detection through Mixture-of-Experts Tuning of Large Language Models](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.12234&hl=en&sa=X&d=18342111694248986737&ei=Dl8FaMQDiKjqtA-e-tPxDg&scisig=AFWwaeYxjMCYW94Z84LR9l2FgOVA&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=2&folt=rel) | Richard Fang |
| LLM | Agent | [Progent: Programmable Privilege Control for LLM Agents](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.11703&hl=en&sa=X&d=12482402578480328066&ei=Dl8FaMQDiKjqtA-e-tPxDg&scisig=AFWwaean05whtIJoVCq_QGoLxbOp&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=3&folt=rel) | Richard Fang |
| Code |  | [Secure Transfer Learning: Training Clean Models Against Backdoor in (Both) Pre-trained Encoders and Downstream Datasets](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.11990&hl=en&sa=X&d=85981534375043028&ei=Dl8FaMQDiKjqtA-e-tPxDg&scisig=AFWwaeaIWCWz5yJjA6srUGUx7MJ1&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=4&folt=rel) | Richard Fang |
| LLM |  | [LLM-Based Automation of COSMIC Functional Size Measurement from Use Cases](https://scholar.google.com/scholar_url?url=https://fpalomba.github.io/pdf/Journals/J77.pdf&hl=en&sa=X&d=10857265925413407421&ei=Dl8FaMQDiKjqtA-e-tPxDg&scisig=AFWwaeYYT0Q2dK2V6Z2SyX7XCGnO&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=5&folt=rel) | Richard Fang |
| LLM |  | [How to Detect and Defeat Molecular Mirage: A Metric-Driven Benchmark for Hallucination in LLM-based Molecular Comprehension](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.12314&hl=en&sa=X&d=16221581542421106752&ei=Dl8FaMQDiKjqtA-e-tPxDg&scisig=AFWwaeZ2t8zQ7arpvf-w8nLaU72M&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=6&folt=rel) | Richard Fang |
|  | Reasoning | [L0-Reasoning Bench: Evaluating Procedural Correctness in Language Models via Simple Program Execution](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.22832&hl=en&sa=X&d=3581934578808224243&ei=Dl8FaMQDiKjqtA-e-tPxDg&scisig=AFWwaebs81HMSqHZ7PO00Lpfwg7f&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=7&folt=rel) | Richard Fang |
| LLM | Agent | [Exploring Expert Failures Improves LLM Agent Tuning](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.13145&hl=en&sa=X&d=5973194658665503274&ei=Dl8FaMQDiKjqtA-e-tPxDg&scisig=AFWwaebJYiIEPQgkQxEuxx20hrR1&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=8&folt=rel) | Richard Fang |
| LLM | Repair, Generation, Agent | [Unlocking LLM Repair Capabilities in Low-Resource Programming Languages Through Cross-Language Translation and Multi-Agent Refinement](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.22512&hl=en&sa=X&d=792507422776186435&ei=Dl8FaMQDiKjqtA-e-tPxDg&scisig=AFWwaeaia2cBVyezePoHp34PQrku&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=9&folt=rel) | Richard Fang |
| APR | Repair | [RePurr: Automated Repair of Block-Based Learners' Programs](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.12445&hl=en&sa=X&d=5861734098693562368&ei=DV8FaOvqMdqs6rQPm9in0A8&scisig=AFWwaebOrtzRJxLZ0-ZeCfHzSyFL&oi=scholaralrt&hist=ylyK0_8AAAAJ:4328508672846969495:AFWwaeZjZJIN-8rhXrY_SmCmGQgD&html=&pos=0&folt=rel) | Bach Le |
| LLM, Code | Generation | [Data-efficient LLM Fine-tuning for Code Generation](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.12687&hl=en&sa=X&d=6940466691581933502&ei=DV8FaIiIOseUywTViqN4&scisig=AFWwaebqIJGq8Ev50ketPcg_AT4z&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=0&folt=rel) | David Lo |
| LLM, Code | Generation | [Malicious and Unintentional Disclosure Risks in Large Language Models for Code Generation](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.22760&hl=en&sa=X&d=2222291530016894533&ei=DV8FaIiIOseUywTViqN4&scisig=AFWwaeYB_Q37ozqUTTfsXXQWnm2a&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=1&folt=rel) | David Lo |
| LLM, Code | Generation | [Code Copycat Conundrum: Demystifying Repetition in LLM-based Code Generation](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.12608&hl=en&sa=X&d=15153918291755445762&ei=DV8FaIiIOseUywTViqN4&scisig=AFWwaeYsVUw-cmkKiP_s8TFLK3te&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=2&folt=rel) | David Lo |
| LLM, Software Testing | Generation | [Automatic High-Level Test Case Generation using Large Language Models](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.17998&hl=en&sa=X&d=2435370287861060433&ei=DV8FaIiIOseUywTViqN4&scisig=AFWwaeb0yzfBEwJ9p6RT6YLxQ0vY&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=4&folt=rel) | David Lo |
| LLM, Code |  | [The Role of Code Readability in Large Language Model Code Summarization](https://scholar.google.com/scholar_url?url=https://www.researchgate.net/profile/Sergey-Yurish/publication/390829629_Advances_in_Signal_Processing_and_Artificial_Intelligence_Proceedings_of_the_7th_International_Conference_on_Advances_in_Signal_Processing_and_Artificial_Intelligence_8-10_April_2025_Innsbruck_Austria/links/67ff7640bfbe974b23aabbd6/Advances-in-Signal-Processing-and-Artificial-Intelligence-Proceedings-of-the-7th-International-Conference-on-Advances-in-Signal-Processing-and-Artificial-Intelligence-8-10-April-2025-Innsbruck-Austri.pdf%23page%3D149&hl=en&sa=X&d=15809233705507088473&ei=DV8FaIiIOseUywTViqN4&scisig=AFWwaeZEzLO7Hst629xs81y1rnQB&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=5&folt=rel) | David Lo |
| Fuzzing, Software Testing | Search | [VLM-Fuzz: Vision Language Model Assisted Recursive Depth-first Search Exploration for Effective UI Testing of Android Apps](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.11675&hl=en&sa=X&d=1988321903897613415&ei=DV8FaIiIOseUywTViqN4&scisig=AFWwaeYt1LWAYgg-W7YeQueDvS05&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=6&folt=rel) | David Lo |
| LLM, Code |  | [LLM Benchmarking with LLaMA2: Evaluating Code Development Performance Across Multiple Programming Languages](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.19217&hl=en&sa=X&d=5827678979979105458&ei=DV8FaIiIOseUywTViqN4&scisig=AFWwaeY1u3h3xWZXb06HdZoeUxgD&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=7&folt=rel) | David Lo |
| LLM, Code, Software Testing, Ethereum |  | [OpDiffer: LLM-Assisted Opcode-Level Differential Testing of Ethereum Virtual Machine](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.12034&hl=en&sa=X&d=2329490431218418572&ei=DV8FaIiIOseUywTViqN4&scisig=AFWwaeaSjhhDKTQsvfZCNVqe-NDA&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=8&folt=rel) | David Lo |
|  |  | [StarFlow: Generating Structured Workflow Outputs From Sketch Images](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.21889%3F&hl=en&sa=X&d=10715069633377113969&ei=DV8FaIiIOseUywTViqN4&scisig=AFWwaebjzq-h_QbWChR82TkIiotu&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=9&folt=rel) | David Lo |
| APR | Repair | [Adapting Knowledge Prompt Tuning for Enhanced Automated Program Repair](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.01523&hl=en&sa=X&d=9461921674059523797&ei=DV8FaKzsNea16rQPhbTBmQc&scisig=AFWwaebGEkQCoR5RF1sA1OAr_sCy&oi=scholaralrt&hist=ylyK0_8AAAAJ:4812769200119993430:AFWwaeYwgMeQSPpxCfDXmGy5aE3n&html=&pos=0&folt=rel) | Thanh Le-Cong |
| Vulnerabilities, LLM | Detection, Reasoning | [Reasoning with LLMs for Zero-Shot Vulnerability Detection](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.17885&hl=en&sa=X&d=16151102993317123730&ei=DV8FaKzsNea16rQPhbTBmQc&scisig=AFWwaeaU1duZG60YHiU0D1fyotku&oi=scholaralrt&hist=ylyK0_8AAAAJ:4812769200119993430:AFWwaeYwgMeQSPpxCfDXmGy5aE3n&html=&pos=2&folt=rel) | Thanh Le-Cong |
|  | Repair | [Enhancing Repository-Level Software Repair via Repository-Aware Knowledge Graphs](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.21710&hl=en&sa=X&d=14440947091517176734&ei=DV8FaKzsNea16rQPhbTBmQc&scisig=AFWwaebBCSzZGxuJdEhcg1ET5UW8&oi=scholaralrt&hist=ylyK0_8AAAAJ:4812769200119993430:AFWwaeYwgMeQSPpxCfDXmGy5aE3n&html=&pos=3&folt=rel) | Thanh Le-Cong |
| LLM, Code | Agent, Reasoning | [CodeARC: Benchmarking Reasoning Capabilities of LLM Agents for Inductive Program Synthesis](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.23145&hl=en&sa=X&d=7322261732284042571&ei=DV8FaKzsNea16rQPhbTBmQc&scisig=AFWwaeaAH4_AfF9MmAImwDIX-Jtw&oi=scholaralrt&hist=ylyK0_8AAAAJ:4812769200119993430:AFWwaeYwgMeQSPpxCfDXmGy5aE3n&html=&pos=5&folt=rel) | Thanh Le-Cong |
| Commit Message | Generation | [Automated Generation of Commit Messages in Software Repositories](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.12998&hl=en&sa=X&d=6245184434680463467&ei=DV8FaKzsNea16rQPhbTBmQc&scisig=AFWwaebHM5kQHptiUgSb4LG5t0up&oi=scholaralrt&hist=ylyK0_8AAAAJ:4812769200119993430:AFWwaeYwgMeQSPpxCfDXmGy5aE3n&html=&pos=6&folt=rel) | Thanh Le-Cong |
| LLM |  | [RepoChat: An LLM-Powered Chatbot for GitHub Repository Question-Answering](https://scholar.google.com/scholar_url?url=https://das.encs.concordia.ca/pdf/abedu2025repochat.pdf&hl=en&sa=X&d=2858684303751462479&ei=DV8FaKzsNea16rQPhbTBmQc&scisig=AFWwaeYP_W9ydFqp7VcvK8oGHT45&oi=scholaralrt&hist=ylyK0_8AAAAJ:4812769200119993430:AFWwaeYwgMeQSPpxCfDXmGy5aE3n&html=&pos=7&folt=rel) | Thanh Le-Cong |
|  | Agent | [ARCeR: an Agentic RAG for the Automated Definition of Cyber Ranges](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.12143&hl=en&sa=X&d=6262779132126183344&ei=DV8FaMKhNPOy6rQP1tr_uA8&scisig=AFWwaeY6gGP0HBLj3a8QyoT54mgW&oi=scholaralrt&hist=ylyK0_8AAAAJ:4436498698466669065:AFWwaebib5Pw9QKWi9BJ6ThKDwc5&html=&pos=0&folt=cit) | Richard Fang |
| Vulnerabilities, LLM | Agent, Exploit | [Teams of LLM Agents can Exploit Zero-Day Vulnerabilities](https://scholar.google.com/scholar_url?url=https://yuxuan18.github.io/assets/pub/teams_of_agents.pdf&hl=en&sa=X&d=17805203639256023308&ei=DV8FaMKhNPOy6rQP1tr_uA8&scisig=AFWwaeZPgyEb6hfnMeK2_WHYixOu&oi=scholaralrt&hist=ylyK0_8AAAAJ:4436498698466669065:AFWwaebib5Pw9QKWi9BJ6ThKDwc5&html=&pos=1&folt=cit) | Richard Fang |
| APR, LLM | Repair | [DALO-APR: LLM-based automatic program repair with data augmentation and loss function optimization](https://scholar.google.com/scholar_url?url=https://link.springer.com/article/10.1007/s11227-025-07102-3&hl=en&sa=X&d=10480458481806281342&ei=Dl8FaMPJAZWrieoPsaHL0Qg&scisig=AFWwaeZgISIeIz-af4x6cYmuf3Oy&oi=scholaralrt&hist=ylyK0_8AAAAJ:16898579961534012346:AFWwaeZADCuvrSiGaZ1pge7b9bMB&html=&pos=0&folt=rel) | Xin ZHOU |
| LLM, Software Testing | Reasoning | [Socrates or Smartypants: Testing Logic Reasoning Capabilities of Large Language Models with Logic Programming-based Test Oracles](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.12312&hl=en&sa=X&d=3686854897724625534&ei=Dl8FaMPJAZWrieoPsaHL0Qg&scisig=AFWwaeYYrn479PXqXdOr9pYNerog&oi=scholaralrt&hist=ylyK0_8AAAAJ:16898579961534012346:AFWwaeZADCuvrSiGaZ1pge7b9bMB&html=&pos=5&folt=rel) | Xin ZHOU |
| Code |  | [Analyzing the impact of prompt engineering on efficiency, code quality, and security in CRUD application development](https://scholar.google.com/scholar_url?url=https://ieeexplore.ieee.org/abstract/document/10963005/&hl=en&sa=X&d=2778415604758727878&ei=DV8FaOn-L5POieoPmpz8kA0&scisig=AFWwaeZXZiQlkYfvWGihi6SwO_gr&oi=scholaralrt&hist=ylyK0_8AAAAJ:1164437029242115036:AFWwaeagPGjpoAfsUTlpD2ZsD6em&html=&pos=0&folt=cit) | Thanh Le-Cong |
| Code |  | [White-box structure analysis of pre-trained language models of code for effective attacking](https://scholar.google.com/scholar_url?url=https://www.sciencedirect.com/science/article/pii/S0950584925000692&hl=en&sa=X&d=10831422306869385650&ei=Dl8FaKatA_mJ6rQP1KeGsAg&scisig=AFWwaeaYut7czcHGT0TluKBywRaC&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=0&folt=rel) | Hong Jin Kang |
| LLM, Code |  | [Large Language Models (LLMs) for Source Code Analysis: applications, models and datasets](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.17502%3F&hl=en&sa=X&d=13932223716190867094&ei=Dl8FaKatA_mJ6rQP1KeGsAg&scisig=AFWwaeaTqZQLIFPcoWmVZF9MztiA&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=2&folt=rel) | Hong Jin Kang |
| Fuzzing |  | [CBGF: Callback Coverage Guided Fuzzing](https://scholar.google.com/scholar_url?url=https://ieeexplore.ieee.org/iel8/6287639/6514899/10965623.pdf&hl=en&sa=X&d=3130441307734811739&ei=Dl8FaKatA_mJ6rQP1KeGsAg&scisig=AFWwaeZoIEFQ_i6JdoG1gUz5tvcM&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=4&folt=rel) | Hong Jin Kang |
| LLM, Code Review, Code |  | [CodeReviewQA: The Code Review Comprehension Assessment for Large Language Models](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.16167&hl=en&sa=X&d=13987149689206803549&ei=Dl8FaKatA_mJ6rQP1KeGsAg&scisig=AFWwaeZRD8EhNW4NSPG4ypaH_WWQ&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=7&folt=rel) | Hong Jin Kang |
| Vulnerabilities, Smart Contracts |  | [Bridging the Gap: A Comparative Study of Academic and Developer Approaches to Smart Contract Vulnerabilities](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.12443&hl=en&sa=X&d=12875937947700763884&ei=DV8FaOC5N8mpieoPm-WPkAQ&scisig=AFWwaeY2zvbbEZ9Bl7QpT3Ieq1wC&oi=scholaralrt&hist=ylyK0_8AAAAJ:4974034551180671527:AFWwaebZb4G2z_XAHxtUtGUOv8go&html=&pos=1&folt=cit) | Bach Le |
|  |  | [Web3 Multimedia Applications: Under the Impact of Decentralization](https://scholar.google.com/scholar_url?url=https://faculty.washington.edu/weicaics/paper/papers/HaoWACLC2025.pdf&hl=en&sa=X&d=3268395530192580864&ei=DV8FaOC5N8mpieoPm-WPkAQ&scisig=AFWwaeaA8doHAMnpAXrImwGUv_Vs&oi=scholaralrt&hist=ylyK0_8AAAAJ:4974034551180671527:AFWwaebZb4G2z_XAHxtUtGUOv8go&html=&pos=2&folt=cit) | Bach Le |
