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
| LLM, Code |  | [The Code Barrier: What LLMs Actually Understand?](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.10557&hl=en&sa=X&d=16959771222072583625&ei=dw4EaOG2LceUywTViqN4&scisig=AFWwaebY9qDBs7QZu6gOkM2zOELP&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=0&folt=rel) | David Lo |
| LLM |  | [MigGPT: Harnessing Large Language Models for Automated Migration of Out-of-Tree Linux Kernel Patches Across Versions](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.09474&hl=en&sa=X&d=1960075332266941840&ei=dw4EaOG2LceUywTViqN4&scisig=AFWwaeaDdG69Y1WbgolcX9e3sh7U&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=1&folt=rel) | David Lo |
| LLM, Software Testing | Generation | [Harnessing Large Language Models for Automated Software Testing: A Leap Towards Scalable Test Case Generation](https://scholar.google.com/scholar_url?url=https://www.researchgate.net/profile/Amro-Al-Said-Ahmad/publication/390492852_Harnessing_Large_Language_Models_for_Automated_Software_Testing_A_Leap_Towards_Scalable_Test_Case_Generation/links/67f0483c76d4923a1af63949/Harnessing-Large-Language-Models-for-Automated-Software-Testing-A-Leap-Towards-Scalable-Test-Case-Generation.pdf&hl=en&sa=X&d=1760969295279974751&ei=dw4EaOG2LceUywTViqN4&scisig=AFWwaeZwjQ9Vuuu06NZk38sjpO70&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=2&folt=rel) | David Lo |
| APR, LLM | Repair | [DALO-APR: LLM-based automatic program repair with data augmentation and loss function optimization](https://scholar.google.com/scholar_url?url=https://link.springer.com/article/10.1007/s11227-025-07102-3&hl=en&sa=X&d=10480458481806281342&ei=dw4EaOG2LceUywTViqN4&scisig=AFWwaeZgISIeIz-af4x6cYmuf3Oy&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=3&folt=rel) | David Lo |
| LLM, Code |  | [LLMigrate: Transforming" Lazy" Large Language Models into Efficient Source Code Migrators](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.23791&hl=en&sa=X&d=8803774605220961224&ei=dw4EaOG2LceUywTViqN4&scisig=AFWwaeY4DQ4Us-xpoOzQ65ucSN24&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=4&folt=rel) | David Lo |
|  | Exploit | [Exploiting Vision-Language Models in GUI Reuse](https://scholar.google.com/scholar_url?url=https://homepages.uc.edu/~niunn/papers/ICSR25.pdf&hl=en&sa=X&d=474069904190286471&ei=dw4EaOG2LceUywTViqN4&scisig=AFWwaeYkLwofQitxvRb0pDXhVL4q&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=5&folt=rel) | David Lo |
|  |  | [Enhancing Just-In-Time Defect Prediction Models with Developer-Centric Features](https://scholar.google.com/scholar_url?url=https://emanuelaguglielmi.it/assets/PDF/JIT-DefectPrediction.pdf&hl=en&sa=X&d=14899542475839495411&ei=dw4EaOG2LceUywTViqN4&scisig=AFWwaeYRKhCxzvAqAugqCHbDf6im&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=6&folt=rel) | David Lo |
| Vulnerabilities, LLM | Agent | [The Obvious Invisible Threat: LLM-Powered GUI Agents' Vulnerability to Fine-Print Injections](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.11281&hl=en&sa=X&d=4014599373074154039&ei=dw4EaOG2LceUywTViqN4&scisig=AFWwaeYmbtsf-Gsj0mCGBCJqi4Mz&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=7&folt=rel) | David Lo |
| LLM | Agent | [Compromising LLM Driven Embodied Agents with Contextual Backdoor Attacks](https://scholar.google.com/scholar_url?url=https://ieeexplore.ieee.org/abstract/document/10943262/&hl=en&sa=X&d=12719951651069852610&ei=dw4EaPijMIio6rQPnvrT8Q4&scisig=AFWwaeZpVIpHx7agj5Gt0-h7Qtt8&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=0&folt=rel) | Richard Fang |
|  | Detection | [DataSentinel: A Game-Theoretic Detection of Prompt Injection Attacks](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.11358&hl=en&sa=X&d=10818935948995424871&ei=dw4EaPijMIio6rQPnvrT8Q4&scisig=AFWwaeZUQoMIWfZAE7jOkiDiHvss&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=1&folt=rel) | Richard Fang |
| LLM |  | [FLUE: Streamlined Uncertainty Estimation for Large Language Models](https://scholar.google.com/scholar_url?url=https://ojs.aaai.org/index.php/AAAI/article/download/33840/35995&hl=en&sa=X&d=12392981900850419093&ei=dw4EaPijMIio6rQPnvrT8Q4&scisig=AFWwaeagkoBV_iGHApqFraS2DENo&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=2&folt=rel) | Richard Fang |
|  |  | [Effective defense against physically embedded backdoor attacks via clustering-based filtering](https://scholar.google.com/scholar_url?url=https://link.springer.com/article/10.1007/s40747-025-01876-y&hl=en&sa=X&d=328651353869364145&ei=dw4EaPijMIio6rQPnvrT8Q4&scisig=AFWwaeYO2KhbA5NjMz2QINArnKei&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=3&folt=rel) | Richard Fang |
| LLM |  | [Exploring Backdoor Attack and Defense for LLM-empowered Recommendations](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.11182&hl=en&sa=X&d=9627500529575121155&ei=dw4EaPijMIio6rQPnvrT8Q4&scisig=AFWwaea16SFNnrAFZnU2vjfGSO8v&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=4&folt=rel) | Richard Fang |
| LLM, Code | Generation | [aiXcoder-7B-v2: Training LLMs to Fully Utilize the Long Context in Repository-level Code Completion](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.15301&hl=en&sa=X&d=15788931866516891147&ei=dw4EaPijMIio6rQPnvrT8Q4&scisig=AFWwaeYi_7K3zAnZWQ5kRBngFmjW&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=5&folt=rel) | Richard Fang |
| LLM, Software Testing | Agent | [Can Large Language Models Trade? Testing Financial Theories with LLM Agents in Market Simulations](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.10789&hl=en&sa=X&d=7842209209030039764&ei=dw4EaPijMIio6rQPnvrT8Q4&scisig=AFWwaebE9A5vGCkYHne57SHvEHs_&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=6&folt=rel) | Richard Fang |
| LLM |  | [L4: Diagnosing large-scale llm training failures via automated log analysis](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.20263&hl=en&sa=X&d=14583207368034027437&ei=dw4EaPijMIio6rQPnvrT8Q4&scisig=AFWwaebRe6Hz8JgakljjX6ZP8ib_&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=7&folt=rel) | Richard Fang |
| LLM |  | [Trajectory Balance with Asynchrony: Decoupling Exploration and Learning for Fast, Scalable LLM Post-Training](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.18929&hl=en&sa=X&d=9558060532125767644&ei=dw4EaPijMIio6rQPnvrT8Q4&scisig=AFWwaeYoVzcxOA7NOnZtm52EYzED&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=8&folt=rel) | Richard Fang |
| LLM |  | [Jenga: Effective Memory Management for Serving LLM with Heterogeneity](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.18292&hl=en&sa=X&d=7739656753816907647&ei=dw4EaPijMIio6rQPnvrT8Q4&scisig=AFWwaebgcPGXUDU8gTuYj4zLJnGn&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=9&folt=rel) | Richard Fang |
| LLM, Code | Generation | [RustEvo^ 2: An Evolving Benchmark for API Evolution in LLM-based Rust Code Generation](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.16922%3F&hl=en&sa=X&d=16675224894932160996&ei=dw4EaNSwKvOy6rQP1tr_uA8&scisig=AFWwaea4g_0zH5bNDjn1WSqwrFGh&oi=scholaralrt&hist=ylyK0_8AAAAJ:4812769200119993430:AFWwaeYwgMeQSPpxCfDXmGy5aE3n&html=&pos=0&folt=rel) | Thanh Le-Cong |
| LLM, Code | Generation | [On Simulation-Guided LLM-based Code Generation for Safe Autonomous Driving Software](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.02141&hl=en&sa=X&d=11030603002805149689&ei=dw4EaNSwKvOy6rQP1tr_uA8&scisig=AFWwaeYUmC_6TmFAo66Flf543eb1&oi=scholaralrt&hist=ylyK0_8AAAAJ:4812769200119993430:AFWwaeYwgMeQSPpxCfDXmGy5aE3n&html=&pos=1&folt=rel) | Thanh Le-Cong |
| LLM, Code |  | [Enhancing Code LLM Training with Programmer Attention](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.14936&hl=en&sa=X&d=18437738178966048662&ei=dw4EaNSwKvOy6rQP1tr_uA8&scisig=AFWwaeYqVjuSDbuyL315ib7n-age&oi=scholaralrt&hist=ylyK0_8AAAAJ:4812769200119993430:AFWwaeYwgMeQSPpxCfDXmGy5aE3n&html=&pos=2&folt=rel) | Thanh Le-Cong |
| Vulnerabilities, Smart Contracts, LLM | Detection | [Smart Contract Vulnerability Detection Using Large Language Models and Graph Structural Analysis.](https://scholar.google.com/scholar_url?url=https://search.ebscohost.com/login.aspx%3Fdirect%3Dtrue%26profile%3Dehost%26scope%3Dsite%26authtype%3Dcrawler%26jrnl%3D15462218%26AN%3D184143386%26h%3DgBiCt2Vo1kRt%252FCK1%252BSWWfB4p5FKnCdgFxhLvS20Pk1p9Cza3sO62Nc8OZpQoxEZ8SeN%252BTYixYvZr7BkNZzwhoA%253D%253D%26crl%3Dc&hl=en&sa=X&d=4504820058459498391&ei=dw4EaNSwKvOy6rQP1tr_uA8&scisig=AFWwaebpASe2BZfIWxlYp5PyJgmc&oi=scholaralrt&hist=ylyK0_8AAAAJ:4812769200119993430:AFWwaeYwgMeQSPpxCfDXmGy5aE3n&html=&pos=3&folt=rel) | Thanh Le-Cong |
| Vulnerabilities, LLM | Detection, Reasoning | [Reasoning with LLMs for Zero-Shot Vulnerability Detection](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.17885&hl=en&sa=X&d=16151102993317123730&ei=dw4EaLfKM9SyieoPgfbI2Qk&scisig=AFWwaeaU1duZG60YHiU0D1fyotku&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=0&folt=rel) | Hong Jin Kang |
| Vulnerabilities | Detection | [Improving distributed learning-based vulnerability detection via multi-modal prompt tuning](https://scholar.google.com/scholar_url?url=https://www.sciencedirect.com/science/article/pii/S0164121225001104&hl=en&sa=X&d=5554212799419582198&ei=dw4EaLfKM9SyieoPgfbI2Qk&scisig=AFWwaebywSeUSc7QcKlN-bBm5POZ&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=1&folt=rel) | Hong Jin Kang |
| LLM, Code | Generation | [Enhancing llm code generation with ensembles: A similarity-based selection approach](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.15838&hl=en&sa=X&d=6315180162277152648&ei=dw4EaLfKM9SyieoPgfbI2Qk&scisig=AFWwaeYw_s8WAmNdUs0l_UHZtKix&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=3&folt=rel) | Hong Jin Kang |
|  |  | [Resolving Conditional Implicit Calls to Improve Static and Dynamic Analysis in Android Apps](https://scholar.google.com/scholar_url?url=https://jordansamhi.com/files/papers/archer.pdf&hl=en&sa=X&d=4455344894030498548&ei=dw4EaLfKM9SyieoPgfbI2Qk&scisig=AFWwaeaw1tkz4SYZ5ffYKxMbPzmn&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=6&folt=rel) | Hong Jin Kang |
| Bug, Software Testing, Static Analysis |  | [BESA: Extending Bugs Triggered by Runtime Testing via Static Analysis](https://scholar.google.com/scholar_url?url=https://dl.acm.org/doi/abs/10.1145/3689031.3696089&hl=en&sa=X&d=11971501184870035235&ei=dw4EaLfKM9SyieoPgfbI2Qk&scisig=AFWwaebDNiyhkoXdOVlEYm5l6Q09&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=7&folt=rel) | Hong Jin Kang |
| Code |  | [Advanced code time complexity prediction approach using contrastive learning](https://scholar.google.com/scholar_url?url=https://www.sciencedirect.com/science/article/pii/S0952197625006311&hl=en&sa=X&d=16349264168467483688&ei=dw4EaLfKM9SyieoPgfbI2Qk&scisig=AFWwaebzdf93mAmknfqCUiHXyi_o&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=8&folt=rel) | Hong Jin Kang |
| LLM, Code |  | [Every Sample Matters: Leveraging Mixture-of-Experts and High-Quality Data for Efficient and Accurate Code LLM](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.17793&hl=en&sa=X&d=6822469255660902021&ei=dw4EaLfKM9SyieoPgfbI2Qk&scisig=AFWwaeZ8vcQc_PT5mFMW0Uih-mYZ&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=9&folt=rel) | Hong Jin Kang |
| APR | Repair | [Adapting Knowledge Prompt Tuning for Enhanced Automated Program Repair](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.01523&hl=en&sa=X&d=9461921674059523797&ei=dw4EaM7jKIWlieoPqbWj8Q4&scisig=AFWwaebGEkQCoR5RF1sA1OAr_sCy&oi=scholaralrt&hist=ylyK0_8AAAAJ:4328508672846969495:AFWwaeZjZJIN-8rhXrY_SmCmGQgD&html=&pos=0&folt=rel) | Bach Le |
