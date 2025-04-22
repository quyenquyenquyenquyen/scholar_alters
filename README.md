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
| APR, LLM | Repair | [Context-aware prompting for LLM-based program repair](https://scholar.google.com/scholar_url?url=https://link.springer.com/article/10.1007/s10515-025-00512-w&hl=en&sa=X&d=3912460072881824433&ei=hKoGaIeTF4WlieoPqbWj8Q4&scisig=AFWwaeYuO0eROorwpxEZoeeWt8hd&oi=scholaralrt&hist=ylyK0_8AAAAJ:4974034551180671527:AFWwaebZb4G2z_XAHxtUtGUOv8go&html=&pos=0&folt=cit) | Bach Le |
|  |  | [uBSaaS: A Unified Blockchain Service as a Service Framework for Streamlined Blockchain Services Integration](https://scholar.google.com/scholar_url?url=https://www.scitepress.org/Papers/2025/133358/133358.pdf&hl=en&sa=X&d=11579980666615008460&ei=hKoGaIeTF4WlieoPqbWj8Q4&scisig=AFWwaea30P44Neopy7wk_SlWNcVO&oi=scholaralrt&hist=ylyK0_8AAAAJ:4974034551180671527:AFWwaebZb4G2z_XAHxtUtGUOv8go&html=&pos=1&folt=cit) | Bach Le |
|  |  | [Leveraging Next-Gen E-Voting Using Proof-of-Stake (PoS) for Secure Elections](https://scholar.google.com/scholar_url?url=https://www.igi-global.com/chapter/leveraging-next-gen-e-voting-using-proof-of-stake-pos-for-secure-elections/376156&hl=en&sa=X&d=10187790774824683082&ei=hKoGaIeTF4WlieoPqbWj8Q4&scisig=AFWwaeZIbEbQ6Vv0deYPlwQ0JsUU&oi=scholaralrt&hist=ylyK0_8AAAAJ:4974034551180671527:AFWwaebZb4G2z_XAHxtUtGUOv8go&html=&pos=2&folt=cit) | Bach Le |
| LLM, Code | Generation | [On Simulation-Guided LLM-based Code Generation for Safe Autonomous Driving Software](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.02141&hl=en&sa=X&d=11030603002805149689&ei=hKoGaL_fFfOy6rQP1tr_uA8&scisig=AFWwaeYUmC_6TmFAo66Flf543eb1&oi=scholaralrt&hist=ylyK0_8AAAAJ:4812769200119993430:AFWwaeYwgMeQSPpxCfDXmGy5aE3n&html=&pos=1&folt=rel) | Thanh Le-Cong |
| Vulnerabilities, Smart Contracts, LLM | Detection | [Smart Contract Vulnerability Detection Using Large Language Models and Graph Structural Analysis.](https://scholar.google.com/scholar_url?url=https://search.ebscohost.com/login.aspx%3Fdirect%3Dtrue%26profile%3Dehost%26scope%3Dsite%26authtype%3Dcrawler%26jrnl%3D15462218%26AN%3D184143386%26h%3DgBiCt2Vo1kRt%252FCK1%252BSWWfB4p5FKnCdgFxhLvS20Pk1p9Cza3sO62Nc8OZpQoxEZ8SeN%252BTYixYvZr7BkNZzwhoA%253D%253D%26crl%3Dc&hl=en&sa=X&d=4504820058459498391&ei=hKoGaL_fFfOy6rQP1tr_uA8&scisig=AFWwaebpASe2BZfIWxlYp5PyJgmc&oi=scholaralrt&hist=ylyK0_8AAAAJ:4812769200119993430:AFWwaeYwgMeQSPpxCfDXmGy5aE3n&html=&pos=2&folt=rel) | Thanh Le-Cong |
| LLM | Agent | [Compromising LLM Driven Embodied Agents with Contextual Backdoor Attacks](https://scholar.google.com/scholar_url?url=https://ieeexplore.ieee.org/abstract/document/10943262/&hl=en&sa=X&d=12719951651069852610&ei=hKoGaNDGG7GyieoPmoPVSA&scisig=AFWwaeZpVIpHx7agj5Gt0-h7Qtt8&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=0&folt=rel) | Richard Fang |
| Code |  | [White-box structure analysis of pre-trained language models of code for effective attacking](https://scholar.google.com/scholar_url?url=https://www.sciencedirect.com/science/article/pii/S0950584925000692&hl=en&sa=X&d=10831422306869385650&ei=hKoGaNDGG7GyieoPmoPVSA&scisig=AFWwaeaYut7czcHGT0TluKBywRaC&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=1&folt=rel) | Richard Fang |
| LLM |  | [L4: Diagnosing large-scale llm training failures via automated log analysis](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.20263&hl=en&sa=X&d=14583207368034027437&ei=hKoGaNDGG7GyieoPmoPVSA&scisig=AFWwaebRe6Hz8JgakljjX6ZP8ib_&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=2&folt=rel) | Richard Fang |
| LLM |  | [Trajectory Balance with Asynchrony: Decoupling Exploration and Learning for Fast, Scalable LLM Post-Training](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.18929&hl=en&sa=X&d=9558060532125767644&ei=hKoGaNDGG7GyieoPmoPVSA&scisig=AFWwaeYoVzcxOA7NOnZtm52EYzED&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=3&folt=rel) | Richard Fang |
| LLM |  | [Jenga: Effective Memory Management for Serving LLM with Heterogeneity](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.18292&hl=en&sa=X&d=7739656753816907647&ei=hKoGaNDGG7GyieoPmoPVSA&scisig=AFWwaebgcPGXUDU8gTuYj4zLJnGn&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=4&folt=rel) | Richard Fang |
| LLM |  | [TiC-LM: A Web-Scale Benchmark for Time-Continual LLM Pretraining](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.02107&hl=en&sa=X&d=214404728453281301&ei=hKoGaNDGG7GyieoPmoPVSA&scisig=AFWwaeaLFt5tc4ITJQUEXtdrdKV4&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=5&folt=rel) | Richard Fang |
|  |  | [Optimizing Language Models for Inference Time Objectives using Reinforcement Learning](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.19595%3F&hl=en&sa=X&d=8707254376221907976&ei=hKoGaNDGG7GyieoPmoPVSA&scisig=AFWwaea3RqIz48sR7GuNBXpH0BvA&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=6&folt=rel) | Richard Fang |
| LLM | Generation | [Automatically Improving LLM-based Verilog Generation using EDA Tool Feedback](https://scholar.google.com/scholar_url?url=https://dl.acm.org/doi/pdf/10.1145/3723876&hl=en&sa=X&d=11120037060516813768&ei=hKoGaNDGG7GyieoPmoPVSA&scisig=AFWwaebvSur0Y23nrD-o0dD19pfz&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=7&folt=rel) | Richard Fang |
| LLM |  | [Whispering Under the Eaves: Protecting User Privacy Against Commercial and LLM-powered Automatic Speech Recognition Systems](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.00858&hl=en&sa=X&d=17126862472531589341&ei=hKoGaNDGG7GyieoPmoPVSA&scisig=AFWwaeacs3ubXF-l97503QMSL1Mt&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=8&folt=rel) | Richard Fang |
| LLM | Reasoning | [DeepSeek-R1 Thoughtology: Let's< think> about LLM Reasoning](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.07128&hl=en&sa=X&d=11093818491604568461&ei=hKoGaNDGG7GyieoPmoPVSA&scisig=AFWwaeY0KvP-dOcXDNdY7ocWzhYS&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=9&folt=rel) | Richard Fang |
| Vulnerabilities, LLM | Detection, Reasoning | [Reasoning with LLMs for Zero-Shot Vulnerability Detection](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.17885&hl=en&sa=X&d=16151102993317123730&ei=hKoGaPnIH8eUywTViqN4&scisig=AFWwaeaU1duZG60YHiU0D1fyotku&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=0&folt=rel) | Hong Jin Kang |
| Bug, Software Testing | Detection | [CTDip: a diversity-guided test program synthesis approach for boosting compiler bug detection](https://scholar.google.com/scholar_url?url=https://link.springer.com/article/10.1007/s10664-025-10642-0&hl=en&sa=X&d=17927180477555540458&ei=hKoGaPnIH8eUywTViqN4&scisig=AFWwaebILt68yqbUH_cAQrtqkdY7&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=1&folt=rel) | Hong Jin Kang |
| LLM, Code |  | [LLMigrate: Transforming" Lazy" Large Language Models into Efficient Source Code Migrators](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.23791&hl=en&sa=X&d=8803774605220961224&ei=hKoGaPnIH8eUywTViqN4&scisig=AFWwaeY4DQ4Us-xpoOzQ65ucSN24&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=2&folt=rel) | Hong Jin Kang |
| Bug, Software Testing, Static Analysis |  | [BESA: Extending Bugs Triggered by Runtime Testing via Static Analysis](https://scholar.google.com/scholar_url?url=https://dl.acm.org/doi/abs/10.1145/3689031.3696089&hl=en&sa=X&d=11971501184870035235&ei=hKoGaPnIH8eUywTViqN4&scisig=AFWwaebDNiyhkoXdOVlEYm5l6Q09&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=3&folt=rel) | Hong Jin Kang |
| Code |  | [Advanced code time complexity prediction approach using contrastive learning](https://scholar.google.com/scholar_url?url=https://www.sciencedirect.com/science/article/pii/S0952197625006311&hl=en&sa=X&d=16349264168467483688&ei=hKoGaPnIH8eUywTViqN4&scisig=AFWwaebzdf93mAmknfqCUiHXyi_o&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=4&folt=rel) | Hong Jin Kang |
| LLM, Code |  | [Every Sample Matters: Leveraging Mixture-of-Experts and High-Quality Data for Efficient and Accurate Code LLM](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.17793&hl=en&sa=X&d=6822469255660902021&ei=hKoGaPnIH8eUywTViqN4&scisig=AFWwaeZ8vcQc_PT5mFMW0Uih-mYZ&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=5&folt=rel) | Hong Jin Kang |
| Fuzzing |  | [Efficient Fuzzing Infrastructure for Pointer-to-Object Association](https://scholar.google.com/scholar_url?url=https://dl.acm.org/doi/pdf/10.1145/3730580&hl=en&sa=X&d=4503812625842861821&ei=hKoGaPnIH8eUywTViqN4&scisig=AFWwaeZjzBNZpNmRSEL69kiYZkzi&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=7&folt=rel) | Hong Jin Kang |
| Bug |  | [An Empirical Study of Rust-Specific Bugs in the rustc Compiler](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.23985&hl=en&sa=X&d=17777641218616878868&ei=hKoGaPnIH8eUywTViqN4&scisig=AFWwaeZ-9atblOv80axiJVZvPuu-&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=9&folt=rel) | Hong Jin Kang |
|  |  | [Artificial Intelligence for Software Engineering: The Journey so far and the Road ahead](https://scholar.google.com/scholar_url?url=https://dl.acm.org/doi/pdf/10.1145/3719006&hl=en&sa=X&d=7262573879989499014&ei=hKoGaOf-EpWrieoPsaHL0Qg&scisig=AFWwaeY7EVIGUJEVmQB0rWf7x8NP&oi=scholaralrt&hist=ylyK0_8AAAAJ:4436498698466669065:AFWwaebib5Pw9QKWi9BJ6ThKDwc5&html=&pos=0&folt=cit) | Richard Fang |
| APR | Repair | [Adapting Knowledge Prompt Tuning for Enhanced Automated Program Repair](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.01523&hl=en&sa=X&d=9461921674059523797&ei=hKoGaIW6EZm7ieoPya6U2A4&scisig=AFWwaebGEkQCoR5RF1sA1OAr_sCy&oi=scholaralrt&hist=ylyK0_8AAAAJ:4328508672846969495:AFWwaeZjZJIN-8rhXrY_SmCmGQgD&html=&pos=0&folt=rel) | Bach Le |
| Code | Detection | [Fine-Grained Code Clone Detection by Keywords-Based Connection of Program Dependency Graph](https://scholar.google.com/scholar_url?url=https://ieeexplore.ieee.org/abstract/document/10967509/&hl=en&sa=X&d=14562124566562428890&ei=hKoGaPLbGMCSieoP_drdwAU&scisig=AFWwaebBqzKIzkMhIcCulLtP40DU&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=2&folt=rel) | David Lo |
| Fuzzing |  | [Fuzzing: On Benchmarking Outcome as a Function of Benchmark Properties](https://scholar.google.com/scholar_url?url=https://abhikrc.com/pdf/TOSEM-fuzzers.pdf&hl=en&sa=X&d=3899393433676860100&ei=hKoGaPLbGMCSieoP_drdwAU&scisig=AFWwaeaeFcyvm9WOp5KG7c6FnRV_&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=3&folt=rel) | David Lo |
| Software Testing | Agent | [ProphetAgent: Automatically Synthesizing GUI Tests from Test Cases in Natural Language for Mobile Apps](https://scholar.google.com/scholar_url?url=https://tingsu.github.io/files/fse2025-ProphetAgent.pdf&hl=en&sa=X&d=7730193664929118236&ei=hKoGaPLbGMCSieoP_drdwAU&scisig=AFWwaeZ6YGFVZwCFt3PMIF5kZaXj&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=4&folt=rel) | David Lo |
