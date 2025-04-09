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
| LLM | Generation | [LLM Test Generation via Iterative Hybrid Program Analysis](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.13580&hl=en&sa=X&d=207857029493572923&ei=XGf1Z9yXOJGu6rQPsO_t0Qo&scisig=AFWwaeYzdRQn3PjIc4QGlsuh6_K4&oi=scholaralrt&hist=ylyK0_8AAAAJ:4328508672846969495:AFWwaeZjZJIN-8rhXrY_SmCmGQgD&html=&pos=0&folt=rel) |
| LLM, Code | Detection | [Potential and Problems in Detecting Privacy Risks in Source Code Using Large Language Models](https://scholar.google.com/scholar_url?url=https://www.pnnl.gov/sites/default/files/media/file/Potential%2520and%2520problems%2520in%2520LLMs%2520Gurjar.pdf&hl=en&sa=X&d=13800682164347660983&ei=XWf1Z-6QCIWlieoPxarRgAo&scisig=AFWwaeZ3JYU11CVzYJE9LRi6ElVT&oi=scholaralrt&hist=ylyK0_8AAAAJ:16898579961534012346:AFWwaeZADCuvrSiGaZ1pge7b9bMB&html=&pos=0&folt=rel) |
| LLM, Code | Generation | [RustEvo^ 2: An Evolving Benchmark for API Evolution in LLM-based Rust Code Generation](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.16922&hl=en&sa=X&d=16675224894932160996&ei=XGf1Z_XcO8mpieoPiM270QI&scisig=AFWwaeZPKPADoJLNBNYGCNV7Grcn&oi=scholaralrt&hist=ylyK0_8AAAAJ:4812769200119993430:AFWwaeYwgMeQSPpxCfDXmGy5aE3n&html=&pos=0&folt=rel) |
| Vulnerabilities, LLM | Detection | [Reasoning with LLMs for Zero-Shot Vulnerability Detection](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.17885&hl=en&sa=X&d=16151102993317123730&ei=XGf1Z_XcO8mpieoPiM270QI&scisig=AFWwaeaU1duZG60YHiU0D1fyotku&oi=scholaralrt&hist=ylyK0_8AAAAJ:4812769200119993430:AFWwaeYwgMeQSPpxCfDXmGy5aE3n&html=&pos=1&folt=rel) |
| LLM, Code | Agent | [LocAgent: Graph-Guided LLM Agents for Code Localization](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.09089%3F&hl=en&sa=X&d=276668227003209980&ei=XWf1Z9jBA-OO6rQP1P-40Q0&scisig=AFWwaebrlhR4TOxAKNYgDQ0UAK82&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=1&folt=rel) |
| Code |  | [OASIS: Order-Augmented Strategy for Improved Code Search](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.08161%3F&hl=en&sa=X&d=15392589071867118103&ei=XWf1Z9jBA-OO6rQP1P-40Q0&scisig=AFWwaea_nsVmM7D1NOV7k0ju42Z6&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=2&folt=rel) |
| Vulnerabilities, Smart Contracts | Detection | [A Vulnerability Detection Method for Smart Contracts Based on Dynamic Meta Optimizer](https://scholar.google.com/scholar_url?url=https://ieeexplore.ieee.org/abstract/document/10948492/&hl=en&sa=X&d=6765480720158859481&ei=XWf1Z9jBA-OO6rQP1P-40Q0&scisig=AFWwaeakeZMPRUQQ-ueaEhmaZCPw&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=3&folt=rel) |
| LLM | Detection | [Bridging the Gap: LLM-Powered Transfer Learning for Log Anomaly Detection in New Software Systems](https://scholar.google.com/scholar_url?url=https://nkcs.iops.ai/wp-content/uploads/2025/03/LogSynergy.pdf&hl=en&sa=X&d=13196007715068821473&ei=XWf1Z9jBA-OO6rQP1P-40Q0&scisig=AFWwaebebvsKdSTwo6qlZVeQLYrz&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=4&folt=rel) |
| Unit Test | Generation | [KotSuite: Unit Test Generation for Kotlin Programs in Android Applications](https://scholar.google.com/scholar_url?url=https://qixin5.github.io/files/pdf/research/icpc25kotsuite.pdf&hl=en&sa=X&d=4160603672644182246&ei=XWf1Z9jBA-OO6rQP1P-40Q0&scisig=AFWwaebk9skrRKkb80KaNdrfD3RV&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=5&folt=rel) |
| LLM |  | [A Multimodal Intelligent Change Assessment Framework for Microservice Systems Based on Large Language Models](https://scholar.google.com/scholar_url?url=https://nkcs.iops.ai/wp-content/uploads/2025/03/ChangeLLM.pdf&hl=en&sa=X&d=2079985240869366990&ei=XWf1Z9jBA-OO6rQP1P-40Q0&scisig=AFWwaeYVBsvXw3_XlXuP3d8xUv2-&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=6&folt=rel) |
| Unit Test, LLM | Generation | [LLM-based Unit Test Generation for Dynamically-Typed Programs](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.14000&hl=en&sa=X&d=7430576131620821752&ei=XWf1Z5CtBpWrieoP3aWvqQM&scisig=AFWwaeY9lDQzBc37lJzEKJmFY6Qx&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=0&folt=rel) |
| LLM |  | [Dancing with Critiques: Enhancing LLM Reasoning with Stepwise Natural Language Self-Critique](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.17363%3F&hl=en&sa=X&d=11521510970677819720&ei=XWf1Z5CtBpWrieoP3aWvqQM&scisig=AFWwaeZ1FoGj3fIwjgWCbOxO43ev&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=2&folt=rel) |
| LLM |  | [CapArena: Benchmarking and Analyzing Detailed Image Captioning in the LLM Era](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.12329%3F&hl=en&sa=X&d=407472380549964642&ei=XWf1Z5CtBpWrieoP3aWvqQM&scisig=AFWwaeYceA6AtNeTroAmdGm1ugPz&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=3&folt=rel) |
| LLM |  | [HalluVerse25: Fine-grained Multilingual Benchmark Dataset for LLM Hallucinations](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.07833&hl=en&sa=X&d=9949819900431535877&ei=XWf1Z5CtBpWrieoP3aWvqQM&scisig=AFWwaebBZBBR2OmH_JGW0bsfEumn&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=4&folt=rel) |
|  |  | [Task-to-Instance Prompt Learning for Vision-Language Models at Test Time](https://scholar.google.com/scholar_url?url=https://ieeexplore.ieee.org/abstract/document/10925517/&hl=en&sa=X&d=7061085335833209582&ei=XWf1Z5CtBpWrieoP3aWvqQM&scisig=AFWwaeauALB5Xz0dtHolj6VGw3Nk&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=5&folt=rel) |
|  |  | [Auditing language models for hidden objectives](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.10965%3F&hl=en&sa=X&d=1501136133567193109&ei=XWf1Z5CtBpWrieoP3aWvqQM&scisig=AFWwaeadoHBh04I6TvMcoaA7ksCs&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=6&folt=rel) |
|  |  | [SuperBPE: Space Travel for Language Models](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.13423&hl=en&sa=X&d=8253915600160210066&ei=XWf1Z5CtBpWrieoP3aWvqQM&scisig=AFWwaeYtH_P2lSDfkM9dWgyLRFRC&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=7&folt=rel) |
|  |  | [Web Artifact Attacks Disrupt Vision Language Models](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.13652&hl=en&sa=X&d=1657536056014156105&ei=XWf1Z5CtBpWrieoP3aWvqQM&scisig=AFWwaeZKlhhb5li7w_A5FieHaObs&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=8&folt=rel) |
| LLM |  | [Enhancing LLM Reasoning with Iterative DPO: A Comprehensive Empirical Investigation](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.12854&hl=en&sa=X&d=6242916882998245282&ei=XWf1Z5CtBpWrieoP3aWvqQM&scisig=AFWwaeaSNyev5Fl1eG07xGIUPECb&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=9&folt=rel) |
|  |  | [The Relationship Between Language Features and PTSD Symptoms: A Systematic Review and Meta-Analysis](https://scholar.google.com/scholar_url?url=https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2025.1476978/pdf&hl=en&sa=X&d=2430309342882977084&ei=XWf1Z62FAZm7ieoP0tiL6Qw&scisig=AFWwaeZsSQf-qi_lTYKggnTyJeqU&oi=scholaralrt&hist=ylyK0_8AAAAJ:4851239734318863641:AFWwaeZ0cPfysy_B7V1I3HcGE9Io&html=&pos=0&folt=cit) |
| LLM |  | [Leveraging large language models for challenge solving in capture-the-flag](https://scholar.google.com/scholar_url?url=https://ieeexplore.ieee.org/abstract/document/10944976/&hl=en&sa=X&d=2373363349342046796&ei=XGf1Z9y1Or6l6rQP-brewAM&scisig=AFWwaeagNg5Uexl4irz7cXhwJGI1&oi=scholaralrt&hist=ylyK0_8AAAAJ:4436498698466669065:AFWwaebib5Pw9QKWi9BJ6ThKDwc5&html=&pos=0&folt=cit) |
| Code |  | [CKTyper: Enhancing Type Inference for Java Code Snippets by Leveraging Crowdsourcing Knowledge in Stack Overflow](https://scholar.google.com/scholar_url?url=https://seal-queensu.github.io/publications/pdf/FSE-Anji-25.pdf&hl=en&sa=X&d=7004309645188894300&ei=XWf1Z925CZWz6rQPzsrEsA8&scisig=AFWwaeYyrjqaFJaDUk1WxX0Qr9lX&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=2&folt=rel) |
| LLM, Code | Generation | [A Comprehensive Study of LLM Secure Code Generation](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.15554%3F&hl=en&sa=X&d=1363137439941333778&ei=XWf1Z925CZWz6rQPzsrEsA8&scisig=AFWwaea70lzbx-2dnx-SlddbyIDc&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=3&folt=rel) |
| LLM, Code | Detection | [Code Clone Detection Techniques Based on Large Language Models](https://scholar.google.com/scholar_url?url=https://ieeexplore.ieee.org/iel8/6287639/6514899/10918947.pdf&hl=en&sa=X&d=10938180619195651115&ei=XWf1Z925CZWz6rQPzsrEsA8&scisig=AFWwaea5cu1UZa40TeDwr8iLOSGG&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=4&folt=rel) |
| Vulnerabilities, LLM | Detection | [Evaluating Biased Synthetic Data Effects on Large Language Model-Based Software Vulnerability Detection](https://scholar.google.com/scholar_url?url=https://www.scitepress.org/Papers/2025/131568/131568.pdf&hl=en&sa=X&d=2607917738470903508&ei=XWf1Z925CZWz6rQPzsrEsA8&scisig=AFWwaeZ0Q2EahjIXC8AC_4u3u9GS&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=5&folt=rel) |
