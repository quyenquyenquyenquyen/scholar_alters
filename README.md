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
|  | Agent | [Technical methods for governing AI agents](https://scholar.google.com/scholar_url?url=https://umontreal.scholaris.ca/bitstreams/e4571c72-a8df-4713-8007-e1dda36b7d27/download&hl=en&sa=X&d=9367667232783575206&ei=Ws_zZ5DrHpWz6rQPzsrEsA8&scisig=AFWwaeZrjEhAnie-XgySRxJXxODF&oi=scholaralrt&hist=ylyK0_8AAAAJ:4436498698466669065:AFWwaebib5Pw9QKWi9BJ6ThKDwc5&html=&pos=0&folt=cit) |
| Large Language Models, Code | Generation | [A Comprehensive Study of LLM Secure Code Generation](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.15554%3F&hl=en&sa=X&d=1363137439941333778&ei=Ws_zZ5eqINSyieoP45Py-Ak&scisig=AFWwaea70lzbx-2dnx-SlddbyIDc&oi=scholaralrt&hist=ylyK0_8AAAAJ:4812769200119993430:AFWwaeYwgMeQSPpxCfDXmGy5aE3n&html=&pos=0&folt=rel) |
| Vulnerabilities, Large Language Models | Detection | [Steering Large Language Models for Vulnerability Detection](https://scholar.google.com/scholar_url?url=https://ieeexplore.ieee.org/abstract/document/10887736/&hl=en&sa=X&d=11396564186480251679&ei=Ws_zZ5eqINSyieoP45Py-Ak&scisig=AFWwaealpmyxj5sAKX0irvJB2uV0&oi=scholaralrt&hist=ylyK0_8AAAAJ:4812769200119993430:AFWwaeYwgMeQSPpxCfDXmGy5aE3n&html=&pos=1&folt=rel) |
| Vulnerabilities, Smart Contracts, Large Language Models | Detection | [Smart Contract Vulnerability Detection Using Large Language Models and Graph Structural Analysis](https://scholar.google.com/scholar_url?url=https://www.sciencedirect.com/org/science/article/pii/S1546221825002504&hl=en&sa=X&d=4504820058459498391&ei=Ws_zZ5eqINSyieoP45Py-Ak&scisig=AFWwaeZMeaniylWwEGOyOdrF9Ulz&oi=scholaralrt&hist=ylyK0_8AAAAJ:4812769200119993430:AFWwaeYwgMeQSPpxCfDXmGy5aE3n&html=&pos=2&folt=rel) |
|  | Exploit | [Exploiting Vision-Language Models in GUI Reuse](https://scholar.google.com/scholar_url?url=https://homepages.uc.edu/~niunn/papers/ICSR25.pdf&hl=en&sa=X&d=474069904190286471&ei=Ws_zZ5eqINSyieoP45Py-Ak&scisig=AFWwaeYkLwofQitxvRb0pDXhVL4q&oi=scholaralrt&hist=ylyK0_8AAAAJ:4812769200119993430:AFWwaeYwgMeQSPpxCfDXmGy5aE3n&html=&pos=3&folt=rel) |
| Large Language Models | Generation | [Harnessing Large Language Models for Automated Software Testing: A Leap Towards Scalable Test Case Generation](https://scholar.google.com/scholar_url?url=https://www.mdpi.com/2079-9292/14/7/1463&hl=en&sa=X&d=1760969295279974751&ei=Ws_zZ6-pJvCj6rQPrrHXyQ4&scisig=AFWwaeYyJa00iJdaXtcAUwgwe9kE&oi=scholaralrt&hist=ylyK0_8AAAAJ:15035864585353249078:AFWwaeZamHljvPChNBtOABcetGTp&html=&pos=0&folt=cit) |
| Large Language Models, Code | Generation | [LLMs Meet Library Evolution: Evaluating Deprecated API Usage in LLM-based Code Completion](https://scholar.google.com/scholar_url?url=https://www.computer.org/csdl/proceedings-article/icse/2025/056900a781/251mHK5tjdC&hl=en&sa=X&d=4291983748355056793&ei=Ws_zZ7X_J4SlieoP2uzx2Aw&scisig=AFWwaebbFgNB42GTnyK8DsY5wt9u&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=0&folt=rel) |
|  | Agent | [Emerging Cyber Attack Risks of Medical AI Agents](https://scholar.google.com/scholar_url?url=https://www.researchgate.net/profile/Jianing-Qiu-2/publication/390450016_Emerging_Cyber_Attack_Risks_of_Medical_AI_Agents/links/67ee4804e8041142a1600c3b/Emerging-Cyber-Attack-Risks-of-Medical-AI-Agents.pdf&hl=en&sa=X&d=11505186898740801309&ei=Ws_zZ7X_J4SlieoP2uzx2Aw&scisig=AFWwaeYfxZWTaaaNgRqjx6QNZTOR&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=1&folt=rel) |
| Vulnerabilities, Verification, Large Language Models | Detection | [Vulnerability Detection: From Formal Verification to Large Language Models and Hybrid Approaches: A Comprehensive Overview](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.10784&hl=en&sa=X&d=12911561823202945144&ei=Ws_zZ7X_J4SlieoP2uzx2Aw&scisig=AFWwaeYhatByJp-efqzH8QuYSI72&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=2&folt=rel) |
|  | Detection | [NaviDet: Efficient Input-level Backdoor Detection on Text-to-Image Synthesis via Neuron Activation Variation](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.06453&hl=en&sa=X&d=12634661584287664552&ei=Ws_zZ7X_J4SlieoP2uzx2Aw&scisig=AFWwaeZmRZs9CfuIOam1tUFWm-wF&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=3&folt=rel) |
| Large Language Models |  | [TiC-LM: A Web-Scale Benchmark for Time-Continual LLM Pretraining](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.02107&hl=en&sa=X&d=214404728453281301&ei=Ws_zZ7X_J4SlieoP2uzx2Aw&scisig=AFWwaeaLFt5tc4ITJQUEXtdrdKV4&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=4&folt=rel) |
|  |  | [VISBIAS: Measuring Explicit and Implicit Social Biases in Vision Language Models](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.07575&hl=en&sa=X&d=4674178038254960174&ei=Ws_zZ7X_J4SlieoP2uzx2Aw&scisig=AFWwaeZypCF53HcST5a-C2B3oJ_r&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=5&folt=rel) |
| Large Language Models |  | [Exposing Product Bias in LLM Investment Recommendation](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.08750%3F&hl=en&sa=X&d=6345310590506339754&ei=Ws_zZ7X_J4SlieoP2uzx2Aw&scisig=AFWwaeb9_8SJP-GsqULJLXGRpplK&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=6&folt=rel) |
| Large Language Models |  | [Process-Supervised LLM Recommenders via Flow-guided Tuning](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.07377&hl=en&sa=X&d=7140189092452996498&ei=Ws_zZ7X_J4SlieoP2uzx2Aw&scisig=AFWwaebI1--hTjcAWg-MbT_UIs8H&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=7&folt=rel) |
| Large Language Models, Code |  | [Every Sample Matters: Leveraging Mixture-of-Experts and High-Quality Data for Efficient and Accurate Code LLM](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.17793&hl=en&sa=X&d=6822469255660902021&ei=Ws_zZ7X_J4SlieoP2uzx2Aw&scisig=AFWwaeZ8vcQc_PT5mFMW0Uih-mYZ&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=8&folt=rel) |
| Large Language Models |  | [CLAIMCHECK: How Grounded are LLM Critiques of Scientific Papers?](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.21717%3F&hl=en&sa=X&d=1023161853858684369&ei=Ws_zZ7X_J4SlieoP2uzx2Aw&scisig=AFWwaebN5U8m2hloOw-jdvceCm44&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=9&folt=rel) |
|  |  | [Benchmarking Failures in Tool-Augmented Language Models](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.14227&hl=en&sa=X&d=12864745453246544967&ei=Ws_zZ9K3I8uZieoP5Y-e4Ao&scisig=AFWwaeZOi6uJnH7_v5ou5yMqdUFy&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=0&folt=rel) |
| Vulnerabilities | Detection | [A software vulnerability detection method based on multi-modality with unified processing](https://scholar.google.com/scholar_url?url=https://www.sciencedirect.com/science/article/pii/S0950584925000424&hl=en&sa=X&d=5319209508677612172&ei=Ws_zZ9K3I8uZieoP5Y-e4Ao&scisig=AFWwaeZxHxmCJPLJLYUF5XxVdqjT&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=1&folt=rel) |
| Unit Test, Large Language Models | Generation | [LLM-based Unit Test Generation for Dynamically-Typed Programs](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.14000&hl=en&sa=X&d=7430576131620821752&ei=Ws_zZ9K3I8uZieoP5Y-e4Ao&scisig=AFWwaeY9lDQzBc37lJzEKJmFY6Qx&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=2&folt=rel) |
| Code | Generation | [Reasoning Through Execution: Unifying Process and Outcome Rewards for Code Generation](https://scholar.google.com/scholar_url?url=https://zhuohaoyu.github.io/assets/files/orps_icml_preprint.pdf&hl=en&sa=X&d=6355483286590305639&ei=Ws_zZ9K3I8uZieoP5Y-e4Ao&scisig=AFWwaeYZVfrCQExVIUTCK0U7b1z0&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=3&folt=rel) |
| Large Language Models |  | [Distinguishing GUI Component States for Blind Users using Large Language Models](https://scholar.google.com/scholar_url?url=https://dl.acm.org/doi/pdf/10.1145/3722106&hl=en&sa=X&d=1868474899543317373&ei=Ws_zZ9K3I8uZieoP5Y-e4Ao&scisig=AFWwaea9XhQBYk3y6qKw_Jww3W_L&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=4&folt=rel) |
| Unit Test, Large Language Models | Generation | [ASTER: Natural and Multi-language Unit Test Generation with LLMs](https://scholar.google.com/scholar_url?url=https://research.ibm.com/publications/aster-natural-and-multi-language-unit-test-generation-with-llms&hl=en&sa=X&d=6207835999541139018&ei=Ws_zZ9K3I8uZieoP5Y-e4Ao&scisig=AFWwaeaSHeQYE6pw7rEso879qVgb&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=5&folt=rel) |
|  |  | [An Empirical Study of Proxy Contracts at the Ethereum Ecosystem Scale](https://scholar.google.com/scholar_url?url=https://mainarke.github.io/assets/papers/icse25_zhang.pdf&hl=en&sa=X&d=17036715211421462991&ei=Ws_zZ9K3I8uZieoP5Y-e4Ao&scisig=AFWwaeYx-iONORw6XFulS3zC4s1O&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=6&folt=rel) |
| Code |  | [AutoGuard: Reporting Breaking Changes of REST APIs from Java Spring Boot Source Code](https://scholar.google.com/scholar_url?url=https://alexx882.github.io/resources/AutoGuard_Paper_preprint_Lercher.pdf&hl=en&sa=X&d=16613358366009630979&ei=Ws_zZ9K3I8uZieoP5Y-e4Ao&scisig=AFWwaean7u0Wy5LmdQZSR019WT35&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=7&folt=rel) |
|  |  | [A Blockchain-Enabled Information as a Service (IaaS) System for Crowdsourced Manufacturing: A Crowdsourcing Case Study of Tank Trailer Manufacturing](https://scholar.google.com/scholar_url?url=https://www.sciencedirect.com/science/article/pii/S2452414X25000688&hl=en&sa=X&d=6249998766361666193&ei=Ws_zZ5neIbGyieoPrY-gmQQ&scisig=AFWwaeaSNx-liE_41-njeBo8gIav&oi=scholaralrt&hist=ylyK0_8AAAAJ:4974034551180671527:AFWwaebZb4G2z_XAHxtUtGUOv8go&html=&pos=0&folt=cit) |
| Vulnerabilities | Detection | [Evaluating LLaMA 3.2 for Software Vulnerability Detection](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.07770%3F&hl=en&sa=X&d=5655905225238348384&ei=Ws_zZ5b3KcmpieoPiM270QI&scisig=AFWwaeaR5pdZsMN2uIoSTXDgghtR&oi=scholaralrt&hist=ylyK0_8AAAAJ:16898579961534012346:AFWwaeZADCuvrSiGaZ1pge7b9bMB&html=&pos=0&folt=rel) |
| Large Language Models | Generation | [LLM-Driven Multi-step Translation from C to Rust using Static Analysis](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.12511&hl=en&sa=X&d=8841093014565201462&ei=Ws_zZ5b3KcmpieoPiM270QI&scisig=AFWwaeaqFbiuIGiODgu9c93gWe3Z&oi=scholaralrt&hist=ylyK0_8AAAAJ:16898579961534012346:AFWwaeZADCuvrSiGaZ1pge7b9bMB&html=&pos=1&folt=rel) |
| Vulnerabilities, Large Language Models, Code | Detection | [VulKiller: Java Web Vulnerability Detection with Code Property Graph and Large Language Models](https://scholar.google.com/scholar_url?url=https://ieeexplore.ieee.org/abstract/document/10890652/&hl=en&sa=X&d=16132470342424149214&ei=Ws_zZ5b3KcmpieoPiM270QI&scisig=AFWwaebtiqQOyVJt5SyK9mTsITpC&oi=scholaralrt&hist=ylyK0_8AAAAJ:16898579961534012346:AFWwaeZADCuvrSiGaZ1pge7b9bMB&html=&pos=3&folt=rel) |
| Large Language Models, Code | Generation | [Enhancing High-Quality Code Generation in Large Language Models with Comparative Prefix-Tuning](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.09020&hl=en&sa=X&d=274986171076802173&ei=Ws_zZ9KZK5m7ieoP0tiL6Qw&scisig=AFWwaea-q7yfbqCfb2mRj_yZrJ7q&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=1&folt=rel) |
| Large Language Models, Code | Generation | [Fixing Large Language Models' Specification Misunderstanding for Better Code Generation](https://scholar.google.com/scholar_url?url=https://drive.google.com/file/d/1eiTmCxYs6FgdxCZNOdS9egz6U1Jf4wOL/view&hl=en&sa=X&d=6513233471596826292&ei=Ws_zZ9KZK5m7ieoP0tiL6Qw&scisig=AFWwaeZjNzZZqbOuWO8MZmi5NgiS&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=2&folt=rel) |
| Unit Test | Generation | [KotSuite: Unit Test Generation for Kotlin Programs in Android Applications](https://scholar.google.com/scholar_url?url=https://qixin5.github.io/files/pdf/research/icpc25kotsuite.pdf&hl=en&sa=X&d=4160603672644182246&ei=Ws_zZ9KZK5m7ieoP0tiL6Qw&scisig=AFWwaebk9skrRKkb80KaNdrfD3RV&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=3&folt=rel) |
| Fuzzing |  | [XMutant: XAI-based Fuzzing for Deep Learning Systems](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.07222&hl=en&sa=X&d=13793734475605200419&ei=Ws_zZ9KZK5m7ieoP0tiL6Qw&scisig=AFWwaeYnfys4dbn96t74wYrCxCKf&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=4&folt=rel) |
| Vulnerabilities, Large Language Models | Exploit | [HALURust: Exploiting Hallucinations of Large Language Models to Detect Vulnerabilities in Rust](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.10793&hl=en&sa=X&d=5829414047755650757&ei=Ws_zZ9KZK5m7ieoP0tiL6Qw&scisig=AFWwaeY9qSDL2ktzIVFeZhrU-G2d&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=5&folt=rel) |
| Large Language Models |  | [RustMap: Towards Project-Scale C-to-Rust Migration via Program Analysis and LLM](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.17741&hl=en&sa=X&d=435714277383772896&ei=Ws_zZ9KZK5m7ieoP0tiL6Qw&scisig=AFWwaeaxm1BWUxxaKhCHs3xYjUtY&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=7&folt=rel) |
