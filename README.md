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
|  |  | [MGC: A modal mapping coupling and gate-driven contrastive learning approach for multimodal intent recognition](https://scholar.google.com/scholar_url?url=https://www.sciencedirect.com/science/article/pii/S0957417425012539&hl=en&sa=X&d=5116476463814215910&ei=sFYCaLLTIIio6rQP9feogAU&scisig=AFWwaeZmw5MjVFiX_HqSDM8FiAsT&oi=scholaralrt&hist=ylyK0_8AAAAJ:4851239734318863641:AFWwaeZ0cPfysy_B7V1I3HcGE9Io&html=&pos=0&folt=cit) | Hong Jin Kang |
| LLM |  | [MigGPT: Harnessing Large Language Models for Automated Migration of Out-of-Tree Linux Kernel Patches Across Versions](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.09474&hl=en&sa=X&d=1960075332266941840&ei=sFYCaLLTIIio6rQP9feogAU&scisig=AFWwaeaDdG69Y1WbgolcX9e3sh7U&oi=scholaralrt&hist=ylyK0_8AAAAJ:4851239734318863641:AFWwaeZ0cPfysy_B7V1I3HcGE9Io&html=&pos=1&folt=cit) | Hong Jin Kang |
| Bug | Detection, Generation | [GitBugs: Bug Reports for Duplicate Detection, Retrieval Augmented Generation, Triage, and More](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.09651&hl=en&sa=X&d=8871451496193637128&ei=sFYCaLLTIIio6rQP9feogAU&scisig=AFWwaebBtv0WvIm-C4TBUnSN4tMQ&oi=scholaralrt&hist=ylyK0_8AAAAJ:4851239734318863641:AFWwaeZ0cPfysy_B7V1I3HcGE9Io&html=&pos=2&folt=cit) | Hong Jin Kang |
| Vulnerabilities, LLM | Detection, Reasoning | [Reasoning with LLMs for Zero-Shot Vulnerability Detection](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.17885&hl=en&sa=X&d=16151102993317123730&ei=sFYCaNSRH5Gu6rQPhJLo-Qk&scisig=AFWwaeaU1duZG60YHiU0D1fyotku&oi=scholaralrt&hist=ylyK0_8AAAAJ:4812769200119993430:AFWwaeYwgMeQSPpxCfDXmGy5aE3n&html=&pos=0&folt=rel) | Thanh Le-Cong |
| LLM, Code | Agent, Reasoning | [CodeARC: Benchmarking Reasoning Capabilities of LLM Agents for Inductive Program Synthesis](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.23145&hl=en&sa=X&d=7322261732284042571&ei=sFYCaNSRH5Gu6rQPhJLo-Qk&scisig=AFWwaeaAH4_AfF9MmAImwDIX-Jtw&oi=scholaralrt&hist=ylyK0_8AAAAJ:4812769200119993430:AFWwaeYwgMeQSPpxCfDXmGy5aE3n&html=&pos=1&folt=rel) | Thanh Le-Cong |
| Code |  | [White-box structure analysis of pre-trained language models of code for effective attacking](https://scholar.google.com/scholar_url?url=https://www.sciencedirect.com/science/article/pii/S0950584925000692&hl=en&sa=X&d=10831422306869385650&ei=sFYCaJ2mKpGu6rQPhJLo-Qk&scisig=AFWwaeaYut7czcHGT0TluKBywRaC&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=0&folt=rel) | Hong Jin Kang |
| LLM, Code |  | [Large Language Models (LLMs) for Source Code Analysis: applications, models and datasets](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.17502&hl=en&sa=X&d=13932223716190867094&ei=sFYCaJ2mKpGu6rQPhJLo-Qk&scisig=AFWwaeb1dh07lugR2sszh6eusTe5&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=1&folt=rel) | Hong Jin Kang |
| Fuzzing |  | [Evaluating API-Level Deep Learning Fuzzers: A Comprehensive Benchmarking Study](https://scholar.google.com/scholar_url?url=https://dl.acm.org/doi/abs/10.1145/3729533&hl=en&sa=X&d=7084698531104603808&ei=sFYCaJ2mKpGu6rQPhJLo-Qk&scisig=AFWwaebLI62cHENmKJRJFgzoOWtS&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=2&folt=rel) | Hong Jin Kang |
|  |  | [Cryptoscope: Analyzing cryptographic usages in modern software](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.19531&hl=en&sa=X&d=6686443909091919827&ei=sFYCaJ2mKpGu6rQPhJLo-Qk&scisig=AFWwaea67RT8XqRdcr5ZIgfReDEG&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=3&folt=rel) | Hong Jin Kang |
| APR, LLM | Repair | [DALO-APR: LLM-based automatic program repair with data augmentation and loss function optimization](https://scholar.google.com/scholar_url?url=https://link.springer.com/article/10.1007/s11227-025-07102-3&hl=en&sa=X&d=10480458481806281342&ei=sFYCaJ2mKpGu6rQPhJLo-Qk&scisig=AFWwaeZgISIeIz-af4x6cYmuf3Oy&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=4&folt=rel) | Hong Jin Kang |
| Software Testing |  | [FANDANGO: Evolving Language-Based Testing](https://scholar.google.com/scholar_url?url=https://publications.cispa.de/articles/conference_contribution/FANDANGO_Evolving_Language-Based_Testing/28769753/1/files/53582009.pdf&hl=en&sa=X&d=9799348799216676838&ei=sFYCaJ2mKpGu6rQPhJLo-Qk&scisig=AFWwaeYGxcve-C-cod8MrX3cSZKA&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=5&folt=rel) | Hong Jin Kang |
| Fuzzing |  | [RAG-Based Fuzzing of Cross-Architecture Compilers](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.08967&hl=en&sa=X&d=18234725876643657828&ei=sFYCaJ2mKpGu6rQPhJLo-Qk&scisig=AFWwaeYdv3A16hwtKYPOY2o9MT03&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=6&folt=rel) | Hong Jin Kang |
| LLM, Software Testing | Generation | [Automatic High-Level Test Case Generation using Large Language Models](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.17998&hl=en&sa=X&d=2435370287861060433&ei=sFYCaJ2mKpGu6rQPhJLo-Qk&scisig=AFWwaeb0yzfBEwJ9p6RT6YLxQ0vY&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=7&folt=rel) | Hong Jin Kang |
| LLM, Code Review, Code |  | [CodeReviewQA: The Code Review Comprehension Assessment for Large Language Models](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.16167&hl=en&sa=X&d=13987149689206803549&ei=sFYCaJ2mKpGu6rQPhJLo-Qk&scisig=AFWwaeZRD8EhNW4NSPG4ypaH_WWQ&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=8&folt=rel) | Hong Jin Kang |
| LLM, Code | Generation | [Enhancing LLM-based Code Translation in Repository Context via Triple Knowledge-Augmented](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.18305&hl=en&sa=X&d=1496301354611823227&ei=sFYCaJ2mKpGu6rQPhJLo-Qk&scisig=AFWwaebZgjNWSGlwwMWRyrQ2cYwe&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=9&folt=rel) | Hong Jin Kang |
| LLM | Agent | [StruPhantom: Evolutionary Injection Attacks on Black-Box Tabular Agents Powered by Large Language Models](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.09841&hl=en&sa=X&d=8898975456969396814&ei=sFYCaKusJua16rQPr6HEKA&scisig=AFWwaeZrl_2--SQtyJrIKCVWjzmL&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=0&folt=rel) | Richard Fang |
| LLM |  | [AdaSteer: Your Aligned LLM is Inherently an Adaptive Jailbreak Defender](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.09466&hl=en&sa=X&d=2341918032029788356&ei=sFYCaKusJua16rQPr6HEKA&scisig=AFWwaebrgnVogbG4VPSgee9degAs&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=1&folt=rel) | Richard Fang |
| LLM |  | [ControlNET: A Firewall for RAG-based LLM System](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.09593&hl=en&sa=X&d=17184153539705524448&ei=sFYCaKusJua16rQPr6HEKA&scisig=AFWwaeYqxdktorXrqpRSjr3bDLUg&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=2&folt=rel) | Richard Fang |
| LLM | Reasoning | [SaRO: Enhancing LLM Safety through Reasoning-based Alignment](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.09420&hl=en&sa=X&d=5520993791348679153&ei=sFYCaKusJua16rQPr6HEKA&scisig=AFWwaeaN4AT63fhFbjcsMxrzqv3X&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=3&folt=rel) | Richard Fang |
| LLM | Reasoning | [Guiding Reasoning in Small Language Models with LLM Assistance](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.09923&hl=en&sa=X&d=14164917725099182845&ei=sFYCaKusJua16rQPr6HEKA&scisig=AFWwaeaZyKC2MhX_kv3y_wekoi1s&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=4&folt=rel) | Richard Fang |
| LLM |  | [XSShield: Defending Against Stored XSS Attacks Using LLM-Based Semantic Understanding](https://scholar.google.com/scholar_url?url=https://www.mdpi.com/2076-3417/15/6/3348&hl=en&sa=X&d=11849643047241211005&ei=sFYCaKusJua16rQPr6HEKA&scisig=AFWwaeZJp-xCesiNk9t9IXhXxSLJ&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=5&folt=rel) | Richard Fang |
| LLM |  | [Dapo: An open-source llm reinforcement learning system at scale](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.14476&hl=en&sa=X&d=1968980266662184520&ei=sFYCaKusJua16rQPr6HEKA&scisig=AFWwaebXNS6d8Y_C8FG4sfvmXe0u&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=6&folt=rel) | Richard Fang |
| LLM | Search | [LLM Social Simulations Are a Promising Research Method](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.02234&hl=en&sa=X&d=16711303184695482252&ei=sFYCaKusJua16rQPr6HEKA&scisig=AFWwaeYGBtI8NvC7VEpsMD3Vz-UB&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=7&folt=rel) | Richard Fang |
| Software Testing | Detection | [Test-Time Backdoor Detection for Object Detection Models](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.15293%3F&hl=en&sa=X&d=6052108469819470987&ei=sFYCaKusJua16rQPr6HEKA&scisig=AFWwaeZFwCtybcnsCXtBxoexifa2&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=8&folt=rel) | Richard Fang |
| LLM |  | [Aligning Multimodal LLM with Human Preference: A Survey](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.14504&hl=en&sa=X&d=1315835665997175613&ei=sFYCaKusJua16rQPr6HEKA&scisig=AFWwaeaYxO6Scdjrz2Sdyj1j9_2t&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=9&folt=rel) | Richard Fang |
| LLM, Software Testing |  | [Benchmarking Practices in LLM-driven Offensive Security: Testbeds, Metrics, and Experiment Design](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.10112&hl=en&sa=X&d=1049283443257479609&ei=sFYCaL7OHeTO6rQPlsna-Qw&scisig=AFWwaeYqMZ5AEX91gvMlww9VDgQQ&oi=scholaralrt&hist=ylyK0_8AAAAJ:4436498698466669065:AFWwaebib5Pw9QKWi9BJ6ThKDwc5&html=&pos=0&folt=cit) | Richard Fang |
| LLM | Agent, Reasoning | [A Survey of Frontiers in LLM Reasoning: Inference Scaling, Learning to Reason, and Agentic Systems](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.09037&hl=en&sa=X&d=12535639908536195100&ei=sFYCaPfrJPOy6rQP0re88AY&scisig=AFWwaebmqOv4WIr3NLEXLWnfHh9g&oi=scholaralrt&hist=ylyK0_8AAAAJ:15035864585353249078:AFWwaeZamHljvPChNBtOABcetGTp&html=&pos=0&folt=cit) | Xin ZHOU |
|  | Generation | [MSCoT: Structured Chain-of-Thought Generation for Multiple Programming Languages](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.10178&hl=en&sa=X&d=3821996461058345675&ei=sFYCaOWsKMeUywTJ0bLoBg&scisig=AFWwaeZoe1lxEPIV49Clg6MndGF0&oi=scholaralrt&hist=ylyK0_8AAAAJ:16898579961534012346:AFWwaeZADCuvrSiGaZ1pge7b9bMB&html=&pos=0&folt=rel) | Xin ZHOU |
| Code |  | [Code-Craft: Hierarchical Graph-Based Code Summarization for Enhanced Context Retrieval](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.08975&hl=en&sa=X&d=13012966678791827914&ei=sFYCaOWsKMeUywTJ0bLoBg&scisig=AFWwaeaOv07lhVW3UYMZqvuTZhS_&oi=scholaralrt&hist=ylyK0_8AAAAJ:16898579961534012346:AFWwaeZADCuvrSiGaZ1pge7b9bMB&html=&pos=2&folt=rel) | Xin ZHOU |
| LLM, Code | Generation | [Uncertainty-Guided Chain-of-Thought for Code Generation with LLMs](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.15341&hl=en&sa=X&d=15218041727249303368&ei=sFYCaOWsKMeUywTJ0bLoBg&scisig=AFWwaeabwVl7WI6ZmTuhEFUfvVBc&oi=scholaralrt&hist=ylyK0_8AAAAJ:16898579961534012346:AFWwaeZADCuvrSiGaZ1pge7b9bMB&html=&pos=3&folt=rel) | Xin ZHOU |
| Fault Localization | Localization | [Evaluating Spectrum-based Fault Localization on Deep Learning Libraries](https://scholar.google.com/scholar_url?url=https://ieeexplore.ieee.org/abstract/document/10930847/&hl=en&sa=X&d=13097586511829065482&ei=sFYCaPyiIpm7ieoPjfnLuQk&scisig=AFWwaeZIPeEWx0xchtsAVxGkT88r&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=1&folt=rel) | David Lo |
| LLM, Software Testing | Generation | [LLM-based Unit Test Generation for Dynamically-Typed Programs](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.14000&hl=en&sa=X&d=7430576131620821752&ei=sFYCaPyiIpm7ieoPjfnLuQk&scisig=AFWwaeY9lDQzBc37lJzEKJmFY6Qx&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=2&folt=rel) | David Lo |
| Code | Generation | [CodeRAG: Supportive Code Retrieval on Bigraph for Real-World Code Generation](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.10046&hl=en&sa=X&d=14720281153510071392&ei=sFYCaPyiIpm7ieoPjfnLuQk&scisig=AFWwaeZLUxRan7HesVUXuzhTEec3&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=3&folt=rel) | David Lo |
| Code |  | [An Empirical Study of the Comparison of Task Recommendation Techniques and Similar Source Code in Open Source Software Projects](https://scholar.google.com/scholar_url?url=https://www.researchsquare.com/article/rs-6322361/latest&hl=en&sa=X&d=7136585553535855548&ei=sFYCaPyiIpm7ieoPjfnLuQk&scisig=AFWwaeZumoxlBxq_sg9en-vbYhdw&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=4&folt=rel) | David Lo |
