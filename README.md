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
| Code | Generation, Agent | [DocAgent: A Multi-Agent System for Automated Code Documentation Generation](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.08725&hl=en&sa=X&d=17391487040813928421&ei=OKwAaKHqNeTO6rQPlsna-Qw&scisig=AFWwaea2ejBoJN0a6J_zGnAekPXP&oi=scholaralrt&hist=ylyK0_8AAAAJ:15035864585353249078:AFWwaeZamHljvPChNBtOABcetGTp&html=&pos=0&folt=cit) |
| Code | Generation | [SelfCodeAlign: Self-Alignment for Code Generation](https://scholar.google.com/scholar_url?url=https://lingming.cs.illinois.edu/publications/neurips2024a.pdf&hl=en&sa=X&d=13342178319076674588&ei=OKwAaKmZM4SlieoPktaN-QY&scisig=AFWwaeY3aA9S3s56bUtMzibeyxLc&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=0&folt=rel) |
| LLM, Software Testing | Detection | [Metamorphic Testing for Fairness Evaluation in Large Language Models: Identifying Intersectional Bias in LLaMA and GPT](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.07982&hl=en&sa=X&d=8291365832876885813&ei=OKwAaKmZM4SlieoPktaN-QY&scisig=AFWwaeZyi3Jp-3LFv6s7E9lgYh2C&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=1&folt=rel) |
| Code |  | [Quality evaluation of Tabby coding assistant using real source code snippets](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.08650&hl=en&sa=X&d=15609747677451661680&ei=OKwAaKmZM4SlieoPktaN-QY&scisig=AFWwaeaWG1SBB5A6wNSBTGDE_bar&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=2&folt=rel) |
| LLM, Software Testing | Agent | [Test Amplification for REST APIs via Single and Multi-Agent LLM Systems](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.08113&hl=en&sa=X&d=12090231993758040543&ei=OKwAaKmZM4SlieoPktaN-QY&scisig=AFWwaeYG4H3F9NsolySjg13ZaZ15&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=3&folt=rel) |
|  |  | [Rethinking Trust in AI Assistants for Software Development: A Critical Review](https://scholar.google.com/scholar_url?url=https://assets.empirical-software.engineering/pdf/tse25-trust-ai-code.pdf&hl=en&sa=X&d=941957821090728764&ei=OKwAaNfbK7GyieoPnei3oQ4&scisig=AFWwaeYRfOQ9-hiKmqHTb0830v39&oi=scholaralrt&hist=ylyK0_8AAAAJ:1164437029242115036:AFWwaeagPGjpoAfsUTlpD2ZsD6em&html=&pos=0&folt=cit) |
| LLM |  | [A comprehensive survey on integrating large language models with knowledge-based methods](https://scholar.google.com/scholar_url?url=https://www.sciencedirect.com/science/article/pii/S0950705125005490&hl=en&sa=X&d=14645346362399576310&ei=OKwAaOHiLvmJ6rQPs4n98A8&scisig=AFWwaebb5VLCuEjXxDH42bc8yd2z&oi=scholaralrt&hist=ylyK0_8AAAAJ:4436498698466669065:AFWwaebib5Pw9QKWi9BJ6ThKDwc5&html=&pos=0&folt=cit) |
| LLM | Agent | [Compromising LLM Driven Embodied Agents with Contextual Backdoor Attacks](https://scholar.google.com/scholar_url?url=https://ieeexplore.ieee.org/abstract/document/10943262/&hl=en&sa=X&d=12719951651069852610&ei=OKwAaMi4N5Gu6rQPhJLo-Qk&scisig=AFWwaeZpVIpHx7agj5Gt0-h7Qtt8&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=0&folt=rel) |
| LLM, Code | Generation | [aiXcoder-7B-v2: Training LLMs to Fully Utilize the Long Context in Repository-level Code Completion](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.15301&hl=en&sa=X&d=15788931866516891147&ei=OKwAaMi4N5Gu6rQPhJLo-Qk&scisig=AFWwaeYi_7K3zAnZWQ5kRBngFmjW&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=1&folt=rel) |
| LLM |  | [L4: Diagnosing large-scale llm training failures via automated log analysis](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.20263&hl=en&sa=X&d=14583207368034027437&ei=OKwAaMi4N5Gu6rQPhJLo-Qk&scisig=AFWwaebRe6Hz8JgakljjX6ZP8ib_&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=2&folt=rel) |
| LLM |  | [Does context matter? contextualjudgebench for evaluating llm-based judges in contextual settings](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.15620&hl=en&sa=X&d=4694277635380098830&ei=OKwAaMi4N5Gu6rQPhJLo-Qk&scisig=AFWwaeZWWBCgHzhwdV7rV4U7IIiY&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=3&folt=rel) |
| LLM |  | [Trajectory Balance with Asynchrony: Decoupling Exploration and Learning for Fast, Scalable LLM Post-Training](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.18929&hl=en&sa=X&d=9558060532125767644&ei=OKwAaMi4N5Gu6rQPhJLo-Qk&scisig=AFWwaeYoVzcxOA7NOnZtm52EYzED&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=4&folt=rel) |
| LLM |  | [Jenga: Effective Memory Management for Serving LLM with Heterogeneity](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.18292&hl=en&sa=X&d=7739656753816907647&ei=OKwAaMi4N5Gu6rQPhJLo-Qk&scisig=AFWwaebgcPGXUDU8gTuYj4zLJnGn&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=5&folt=rel) |
| LLM | Reasoning | [Enhancing LLM Reasoning with Iterative DPO: A Comprehensive Empirical Investigation](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.12854%3F&hl=en&sa=X&d=6242916882998245282&ei=OKwAaMi4N5Gu6rQPhJLo-Qk&scisig=AFWwaeas1YS6MF9XYtnthgs4xm8W&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=6&folt=rel) |
| LLM |  | [Navigating Rifts in Human-LLM Grounding: Study and Benchmark](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.13975&hl=en&sa=X&d=6056628797355529511&ei=OKwAaMi4N5Gu6rQPhJLo-Qk&scisig=AFWwaeYuzwNKVc6ZCL0NUy7wCU7P&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=7&folt=rel) |
|  |  | [Parameters vs. Context: Fine-Grained Control of Knowledge Reliance in Language Models](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.15888&hl=en&sa=X&d=8358907449720691769&ei=OKwAaMi4N5Gu6rQPhJLo-Qk&scisig=AFWwaeZPIqjVcxmMuI4nDW3DhW3i&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=8&folt=rel) |
|  |  | [Superbpe: Space travel for language models](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.13423&hl=en&sa=X&d=8253915600160210066&ei=OKwAaMi4N5Gu6rQPhJLo-Qk&scisig=AFWwaeYtH_P2lSDfkM9dWgyLRFRC&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=9&folt=rel) |
| LLM, Code | Generation | [RustEvo^ 2: An Evolving Benchmark for API Evolution in LLM-based Rust Code Generation](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.16922%3F&hl=en&sa=X&d=16675224894932160996&ei=OKwAaJieMJuw6rQP7-68qA0&scisig=AFWwaea4g_0zH5bNDjn1WSqwrFGh&oi=scholaralrt&hist=ylyK0_8AAAAJ:4812769200119993430:AFWwaeYwgMeQSPpxCfDXmGy5aE3n&html=&pos=0&folt=rel) |
| Vulnerabilities, Smart Contracts, LLM | Detection | [Smart Contract Vulnerability Detection Using Large Language Models and Graph Structural Analysis](https://scholar.google.com/scholar_url?url=https://www.sciencedirect.com/org/science/article/pii/S1546221825002504&hl=en&sa=X&d=4504820058459498391&ei=OKwAaJieMJuw6rQP7-68qA0&scisig=AFWwaeZMeaniylWwEGOyOdrF9Ulz&oi=scholaralrt&hist=ylyK0_8AAAAJ:4812769200119993430:AFWwaeYwgMeQSPpxCfDXmGy5aE3n&html=&pos=1&folt=rel) |
| Vulnerabilities, LLM | Detection, Reasoning | [Reasoning with LLMs for Zero-Shot Vulnerability Detection](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.17885&hl=en&sa=X&d=16151102993317123730&ei=OKwAaIuDOcmpieoPnPbKsA4&scisig=AFWwaeaU1duZG60YHiU0D1fyotku&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=0&folt=rel) |
| LLM, Code | Generation | [Enhancing llm code generation with ensembles: A similarity-based selection approach](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.15838&hl=en&sa=X&d=6315180162277152648&ei=OKwAaIuDOcmpieoPnPbKsA4&scisig=AFWwaeYw_s8WAmNdUs0l_UHZtKix&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=1&folt=rel) |
| LLM, Fuzzing, Software Testing | Generation | [Intelligent Test Case Generation Method for Fuzzing IoT Protocols Based on LLM](https://scholar.google.com/scholar_url?url=https://www.researchsquare.com/article/rs-6331846/latest&hl=en&sa=X&d=7977717061909231178&ei=OKwAaIuDOcmpieoPnPbKsA4&scisig=AFWwaeapZ-qmTHpSU3vKd7fjLdqF&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=3&folt=rel) |
| Bug, Software Testing, Static Analysis |  | [BESA: Extending Bugs Triggered by Runtime Testing via Static Analysis](https://scholar.google.com/scholar_url?url=https://dl.acm.org/doi/abs/10.1145/3689031.3696089&hl=en&sa=X&d=11971501184870035235&ei=OKwAaIuDOcmpieoPnPbKsA4&scisig=AFWwaebDNiyhkoXdOVlEYm5l6Q09&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=4&folt=rel) |
| LLM, Code |  | [Every Sample Matters: Leveraging Mixture-of-Experts and High-Quality Data for Efficient and Accurate Code LLM](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.17793&hl=en&sa=X&d=6822469255660902021&ei=OKwAaIuDOcmpieoPnPbKsA4&scisig=AFWwaeZ8vcQc_PT5mFMW0Uih-mYZ&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=5&folt=rel) |
| LLM, Code | Generation | [A Comprehensive Study of LLM Secure Code Generation](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.15554%3F&hl=en&sa=X&d=1363137439941333778&ei=OKwAaIuDOcmpieoPnPbKsA4&scisig=AFWwaea70lzbx-2dnx-SlddbyIDc&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=6&folt=rel) |
| LLM, Code, Software Testing |  | [Automated Harmfulness Testing for Code Large Language Models](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.16740&hl=en&sa=X&d=9984898886618882508&ei=OKwAaIuDOcmpieoPnPbKsA4&scisig=AFWwaeY9TKp5hroYtjAXp0K1dUfY&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=7&folt=rel) |
| LLM, Software Testing | Generation | [LSPAI: An IDE Plugin for LLM-Powered Multi-Language Unit Test Generation with Language Server Protocol](https://scholar.google.com/scholar_url?url=https://gwihwan-go.github.io/files/papers/fse-industry-LSPAI-v1.pdf&hl=en&sa=X&d=11950018507395283255&ei=OKwAaIuDOcmpieoPnPbKsA4&scisig=AFWwaea7SQm3uWdWdA_CN8rRFfhT&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=9&folt=rel) |
