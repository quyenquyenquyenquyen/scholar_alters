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
| LLM, Code |  | [OpenCodeInstruct: A Large-scale Instruction Tuning Dataset for Code LLMs](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.04030&hl=en&sa=X&d=5917653904305649400&ei=2Ub4Z-XTEY-j6rQPo73a4AM&scisig=AFWwaeaybbbls4eyzwf1B3I5oC44&oi=scholaralrt&hist=ylyK0_8AAAAJ:4812769200119993430:AFWwaeYwgMeQSPpxCfDXmGy5aE3n&html=&pos=0&folt=rel) |
| LLM, Code |  | [How Accurately Do Large Language Models Understand Code?](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.04372&hl=en&sa=X&d=13848317151172529366&ei=2Ub4Z-XTEY-j6rQPo73a4AM&scisig=AFWwaeaAEeCieX1LHkvPVUHyVgKS&oi=scholaralrt&hist=ylyK0_8AAAAJ:4812769200119993430:AFWwaeYwgMeQSPpxCfDXmGy5aE3n&html=&pos=1&folt=rel) |
| LLM, Code | Generation | [RustEvo^ 2: An Evolving Benchmark for API Evolution in LLM-based Rust Code Generation](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.16922%3F&hl=en&sa=X&d=16675224894932160996&ei=2Ub4Z-XTEY-j6rQPo73a4AM&scisig=AFWwaea4g_0zH5bNDjn1WSqwrFGh&oi=scholaralrt&hist=ylyK0_8AAAAJ:4812769200119993430:AFWwaeYwgMeQSPpxCfDXmGy5aE3n&html=&pos=2&folt=rel) |
|  |  | [L0-Reasoning Bench: Evaluating Procedural Correctness in Language Models via Simple Program Execution](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.22832&hl=en&sa=X&d=3581934578808224243&ei=2Ub4Z-XTEY-j6rQPo73a4AM&scisig=AFWwaebs81HMSqHZ7PO00Lpfwg7f&oi=scholaralrt&hist=ylyK0_8AAAAJ:4812769200119993430:AFWwaeYwgMeQSPpxCfDXmGy5aE3n&html=&pos=3&folt=rel) |
| LLM, Software Testing | Generation | [LLM Test Generation via Iterative Hybrid Program Analysis](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.13580&hl=en&sa=X&d=207857029493572923&ei=2Ub4Z-XTEY-j6rQPo73a4AM&scisig=AFWwaeYzdRQn3PjIc4QGlsuh6_K4&oi=scholaralrt&hist=ylyK0_8AAAAJ:4812769200119993430:AFWwaeYwgMeQSPpxCfDXmGy5aE3n&html=&pos=4&folt=rel) |
| LLM, Code | Generation | [DDPT: Diffusion-Driven Prompt Tuning for Large Language Model Code Generation](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.04351&hl=en&sa=X&d=10777735064745098709&ei=2Ub4Z_b5FZuw6rQPjdfcmQQ&scisig=AFWwaeZu_rFKtOje-Q7rbJBNmDlF&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=1&folt=rel) |
| LLM, Code | Agent, Localization | [LocAgent: Graph-Guided LLM Agents for Code Localization](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.09089%3F&hl=en&sa=X&d=276668227003209980&ei=2Ub4Z_b5FZuw6rQPjdfcmQQ&scisig=AFWwaebrlhR4TOxAKNYgDQ0UAK82&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=2&folt=rel) |
| Vulnerabilities, Smart Contracts, LLM | Detection | [Generative Large Language Model usage in Smart Contract Vulnerability Detection](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.04685&hl=en&sa=X&d=3782065939597708655&ei=2Ub4Z_b5FZuw6rQPjdfcmQQ&scisig=AFWwaeZid-0xDC6cki9Q59anhPrN&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=5&folt=rel) |
| Code | Search | [OASIS: Order-Augmented Strategy for Improved Code Search](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.08161%3F&hl=en&sa=X&d=15392589071867118103&ei=2Ub4Z_b5FZuw6rQPjdfcmQQ&scisig=AFWwaea_nsVmM7D1NOV7k0ju42Z6&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=6&folt=rel) |
| Vulnerabilities, Smart Contracts, Code, Bug | Detection | [SmartBugBert: BERT-Enhanced Vulnerability Detection for Smart Contract Bytecode](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.05002&hl=en&sa=X&d=6150372104347240756&ei=2Ub4Z_b5FZuw6rQPjdfcmQQ&scisig=AFWwaeb2WS1H06_-kEaW3oJ1KhL-&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=7&folt=rel) |
| Vulnerabilities, Smart Contracts, LLM | Detection | [Enhancing Smart Contract Vulnerability Detection in DApps Leveraging Fine-Tuned LLM](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.05006&hl=en&sa=X&d=3716949235882934426&ei=2Ub4Z_b5FZuw6rQPjdfcmQQ&scisig=AFWwaeYhOxTQXubByPB5TSI1XIvX&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=8&folt=rel) |
| LLM, Code, Bug |  | [LLMs are Bug Replicators: An Empirical Study on LLMs' Capability in Completing Bug-prone Code](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.11082&hl=en&sa=X&d=9189825353695587011&ei=2Ub4Z_b5FZuw6rQPjdfcmQQ&scisig=AFWwaeZYDliimmo8dCt2DNKqsCtm&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=9&folt=rel) |
| Code | Generation | [An Evaluation of the Impact of Code Generation Tools on Software Development](https://scholar.google.com/scholar_url?url=https://sol.sbc.org.br/index.php/sbsi/article/download/34379/34170/&hl=en&sa=X&d=3475411260493206906&ei=2Ub4Z-_NFJWz6rQPveLUmAo&scisig=AFWwaea7SKoUpbPD5bymc7jUS7ef&oi=scholaralrt&hist=ylyK0_8AAAAJ:4974034551180671527:AFWwaebZb4G2z_XAHxtUtGUOv8go&html=&pos=0&folt=cit) |
| Vulnerabilities |  | [R2Vul: Learning to Reason about Software Vulnerabilities with Reinforcement Learning and Structured Reasoning Distillation](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.04699&hl=en&sa=X&d=5785686524278912976&ei=2Ub4Z8zsG-OO6rQPq-P-gAo&scisig=AFWwaebENSFvsakJL8hNltnJjy6R&oi=scholaralrt&hist=ylyK0_8AAAAJ:16898579961534012346:AFWwaeZADCuvrSiGaZ1pge7b9bMB&html=&pos=3&folt=rel) |
| LLM, Code, Software Testing | Generation | [Evaluating the Role of Large Language Models in Test Configuration Code Generation: An Empirical Study](https://scholar.google.com/scholar_url?url=https://www.diva-portal.org/smash/record.jsf%3Fpid%3Ddiva2:1949520&hl=en&sa=X&d=13946686766702512593&ei=2Ub4Z9HfGJGu6rQPyMPCuAs&scisig=AFWwaebZjl6pcp_F69N4Jbybj5o2&oi=scholaralrt&hist=ylyK0_8AAAAJ:15035864585353249078:AFWwaeZamHljvPChNBtOABcetGTp&html=&pos=0&folt=cit) |
| LLM, Code Review, Code |  | [Leveraging Large Language Models for Security-Focused Code Reviews](https://scholar.google.com/scholar_url?url=https://adsecvn.com/wp-content/uploads/2025/03/LLM_Code_Reviews.pdf&hl=en&sa=X&d=10362399872801253051&ei=2Ub4Z9HfGJGu6rQPyMPCuAs&scisig=AFWwaeZAJvF78KyLNU_FomXddKVU&oi=scholaralrt&hist=ylyK0_8AAAAJ:15035864585353249078:AFWwaeZamHljvPChNBtOABcetGTp&html=&pos=1&folt=cit) |
|  | Agent | [ELT-Bench: An End-to-End Benchmark for Evaluating AI Agents on ELT Pipelines](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.04808&hl=en&sa=X&d=17618773598726971491&ei=2Ub4Z-aMGr6l6rQP6IGIqAI&scisig=AFWwaeZtqP-28GczAcquqwQEokUH&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=0&folt=rel) |
|  | Agent | [Emerging Cyber Attack Risks of Medical AI Agents](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.03759&hl=en&sa=X&d=2197394737877831403&ei=2Ub4Z-aMGr6l6rQP6IGIqAI&scisig=AFWwaeaDfSE-QTy5FZtsSiO83H84&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=1&folt=rel) |
| LLM | Agent | [Les Dissonances: Cross-Tool Harvesting and Polluting in Multi-Tool Empowered LLM Agents](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.03111&hl=en&sa=X&d=16787567624520007863&ei=2Ub4Z-aMGr6l6rQP6IGIqAI&scisig=AFWwaeZ1aVR1vsCpBgrDw-H6FAoH&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=2&folt=rel) |
| LLM, Software Testing | Generation | [LLM-based Unit Test Generation for Dynamically-Typed Programs](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.14000&hl=en&sa=X&d=7430576131620821752&ei=2Ub4Z-aMGr6l6rQP6IGIqAI&scisig=AFWwaeY9lDQzBc37lJzEKJmFY6Qx&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=3&folt=rel) |
| LLM |  | [Does context matter? contextualjudgebench for evaluating llm-based judges in contextual settings](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.15620&hl=en&sa=X&d=4694277635380098830&ei=2Ub4Z-aMGr6l6rQP6IGIqAI&scisig=AFWwaeZWWBCgHzhwdV7rV4U7IIiY&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=6&folt=rel) |
| LLM |  | [Dancing with Critiques: Enhancing LLM Reasoning with Stepwise Natural Language Self-Critique](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.17363%3F&hl=en&sa=X&d=11521510970677819720&ei=2Ub4Z-aMGr6l6rQP6IGIqAI&scisig=AFWwaeZ1FoGj3fIwjgWCbOxO43ev&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=7&folt=rel) |
| LLM |  | [CapArena: Benchmarking and Analyzing Detailed Image Captioning in the LLM Era](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.12329%3F&hl=en&sa=X&d=407472380549964642&ei=2Ub4Z-aMGr6l6rQP6IGIqAI&scisig=AFWwaeYceA6AtNeTroAmdGm1ugPz&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=8&folt=rel) |
| LLM |  | [Navigating Rifts in Human-LLM Grounding: Study and Benchmark](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.13975&hl=en&sa=X&d=6056628797355529511&ei=2Ub4Z-aMGr6l6rQP6IGIqAI&scisig=AFWwaeYuzwNKVc6ZCL0NUy7wCU7P&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=9&folt=rel) |
|  |  | [Knowledge Representation for Integrating Clinical and Administrative Data in Claims Processing](https://scholar.google.com/scholar_url?url=https://kernpublic.com/index.php/IJDSBDAPM/article/download/2025-MARCH-04/4&hl=en&sa=X&d=9620520256098350845&ei=2Ub4Z96YE5m7ieoP3oH9uAU&scisig=AFWwaeYbWw_qcdEPlQ5a0pp8NRXZ&oi=scholaralrt&hist=ylyK0_8AAAAJ:4851239734318863641:AFWwaeZ0cPfysy_B7V1I3HcGE9Io&html=&pos=0&folt=cit) |
|  |  | [The H-Elena Trojan Virus to Infect Model Weights: A Wake-Up Call on the Security Risks of Malicious Fine-Tuning](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.03823&hl=en&sa=X&d=4497889825907294098&ei=2Ub4Z96YE5m7ieoP3oH9uAU&scisig=AFWwaeawnUsLCfgYu5MTYKwR1IZS&oi=scholaralrt&hist=ylyK0_8AAAAJ:4851239734318863641:AFWwaeZ0cPfysy_B7V1I3HcGE9Io&html=&pos=1&folt=cit) |
| Bug |  | [HaPy-Bug--Human Annotated Python Bug Resolution Dataset](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.04810&hl=en&sa=X&d=14796298888512808939&ei=2Ub4Z96YE5m7ieoP3oH9uAU&scisig=AFWwaeYeuxs95UiH0nX0RS_Hq0VE&oi=scholaralrt&hist=ylyK0_8AAAAJ:4851239734318863641:AFWwaeZ0cPfysy_B7V1I3HcGE9Io&html=&pos=3&folt=cit) |
| LLM |  | [Toward LLM-Driven GDPR Compliance Checking for Android Apps](https://scholar.google.com/scholar_url?url=https://orbilu.uni.lu/bitstream/10993/64674/1/FSE_IVR_2025_RegCheck.pdf&hl=en&sa=X&d=9430644475903485929&ei=2Ub4Z47WHZWrieoPtfXHiQw&scisig=AFWwaeY9mg3zPUX9ptxQyzP3T_Nw&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=3&folt=rel) |
|  |  | [Do Developers Depend on Deprecated Library Versions? A Mining Study of Log4j](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.03167&hl=en&sa=X&d=17142084561539849326&ei=2Ub4Z47WHZWrieoPtfXHiQw&scisig=AFWwaeaX8kuemmCFKNqJ5rQtzpsR&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=4&folt=rel) |
| Bug, Software Testing, Static Analysis |  | [BESA: Extending Bugs Triggered by Runtime Testing via Static Analysis](https://scholar.google.com/scholar_url?url=https://dl.acm.org/doi/abs/10.1145/3689031.3696089&hl=en&sa=X&d=11971501184870035235&ei=2Ub4Z47WHZWrieoPtfXHiQw&scisig=AFWwaebDNiyhkoXdOVlEYm5l6Q09&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=5&folt=rel) |
| LLM, Code | Generation | [A Comprehensive Study of LLM Secure Code Generation](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.15554%3F&hl=en&sa=X&d=1363137439941333778&ei=2Ub4Z47WHZWrieoPtfXHiQw&scisig=AFWwaea70lzbx-2dnx-SlddbyIDc&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=6&folt=rel) |
| Vulnerabilities, Code | Detection | [Automatic Software Vulnerability Detection in Binary Code](https://scholar.google.com/scholar_url?url=https://books.google.com/books%3Fhl%3Den%26lr%3Dlang_en%26id%3DgtJSEQAAQBAJ%26oi%3Dfnd%26pg%3DPA148%26ots%3D4r_QwP4uxA%26sig%3DcvmUxVdJjhji1ZVTJ5iM3lu67oM&hl=en&sa=X&d=8963754288088414031&ei=2Ub4Z47WHZWrieoPtfXHiQw&scisig=AFWwaeZep79dGvTHXvqqfWTiFBYy&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=9&folt=rel) |
