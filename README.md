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
|  | Repair | [We've Got You Covered: Type-Guided Repair of Incomplete Input Generators](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.06421&hl=en&sa=X&d=4537435868289132628&ei=3tz6Z9nVBpWz6rQPveLUmAo&scisig=AFWwaeZY_M8Dee75x_6YAOvVVoRP&oi=scholaralrt&hist=ylyK0_8AAAAJ:4974034551180671527:AFWwaebZb4G2z_XAHxtUtGUOv8go&html=&pos=0&folt=cit) |
| Vulnerabilities | Repair | [Using ML filters to help automated vulnerability repairs: when it helps and when it doesn't](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.07027&hl=en&sa=X&d=8016374535122276286&ei=3tz6Z9nVBpWz6rQPveLUmAo&scisig=AFWwaeaaxwymeGrLM10a1ld5ymOL&oi=scholaralrt&hist=ylyK0_8AAAAJ:4974034551180671527:AFWwaebZb4G2z_XAHxtUtGUOv8go&html=&pos=1&folt=cit) |
|  | Localization | [PAFL: Enhancing Fault Localizers by Leveraging Project-Specific Fault Patterns](https://scholar.google.com/scholar_url?url=https://dl.acm.org/doi/pdf/10.1145/3720526&hl=en&sa=X&d=18081862642413033156&ei=3tz6Z-7oA5yV6rQP8q-dkA0&scisig=AFWwaebn1piFwIZdyjc2aafeRxly&oi=scholaralrt&hist=ylyK0_8AAAAJ:4812769200119993430:AFWwaeYwgMeQSPpxCfDXmGy5aE3n&html=&pos=0&folt=rel) |
| LLM, Code | Generation | [RustEvo^ 2: An Evolving Benchmark for API Evolution in LLM-based Rust Code Generation](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.16922%3F&hl=en&sa=X&d=16675224894932160996&ei=3tz6Z-7oA5yV6rQP8q-dkA0&scisig=AFWwaea4g_0zH5bNDjn1WSqwrFGh&oi=scholaralrt&hist=ylyK0_8AAAAJ:4812769200119993430:AFWwaeYwgMeQSPpxCfDXmGy5aE3n&html=&pos=2&folt=rel) |
| LLM, Software Testing | Generation | [LLM Test Generation via Iterative Hybrid Program Analysis](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.13580&hl=en&sa=X&d=207857029493572923&ei=3tz6Z-7oA5yV6rQP8q-dkA0&scisig=AFWwaeYzdRQn3PjIc4QGlsuh6_K4&oi=scholaralrt&hist=ylyK0_8AAAAJ:4812769200119993430:AFWwaeYwgMeQSPpxCfDXmGy5aE3n&html=&pos=3&folt=rel) |
| Vulnerabilities, Smart Contracts, LLM | Detection | [Smart Contract Vulnerability Detection Using Large Language Models and Graph Structural Analysis](https://scholar.google.com/scholar_url?url=https://www.sciencedirect.com/org/science/article/pii/S1546221825002504&hl=en&sa=X&d=4504820058459498391&ei=3tz6Z-7oA5yV6rQP8q-dkA0&scisig=AFWwaeZMeaniylWwEGOyOdrF9Ulz&oi=scholaralrt&hist=ylyK0_8AAAAJ:4812769200119993430:AFWwaeYwgMeQSPpxCfDXmGy5aE3n&html=&pos=4&folt=rel) |
| LLM, Code | Agent, Localization | [LocAgent: Graph-Guided LLM Agents for Code Localization](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.09089%3F&hl=en&sa=X&d=276668227003209980&ei=3tz6Z-7oA5yV6rQP8q-dkA0&scisig=AFWwaebrlhR4TOxAKNYgDQ0UAK82&oi=scholaralrt&hist=ylyK0_8AAAAJ:4812769200119993430:AFWwaeYwgMeQSPpxCfDXmGy5aE3n&html=&pos=5&folt=rel) |
| LLM |  | [Optimizing Large Language Models: Metrics, Energy Efficiency, and Case Study Insights](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.06307&hl=en&sa=X&d=6387174928915548778&ei=3tz6Z_agBY-j6rQPo73a4AM&scisig=AFWwaeZsppe_Gg9AId0scfgh7vgW&oi=scholaralrt&hist=ylyK0_8AAAAJ:4851239734318863641:AFWwaeZ0cPfysy_B7V1I3HcGE9Io&html=&pos=0&folt=cit) |
| Code | Detection | [DeCoMa: Detecting and Purifying Code Dataset Watermarks through Dual Channel Code Abstraction](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.07002&hl=en&sa=X&d=15919972095243974215&ei=3tz6Z_agBY-j6rQPo73a4AM&scisig=AFWwaeYiPCmm16yztgJgTf31LLj0&oi=scholaralrt&hist=ylyK0_8AAAAJ:4851239734318863641:AFWwaeZ0cPfysy_B7V1I3HcGE9Io&html=&pos=1&folt=cit) |
| Vulnerabilities, Code | Detection | [VDMAF: Cross-language source code vulnerability detection using multi-head attention fusion](https://scholar.google.com/scholar_url?url=https://www.sciencedirect.com/science/article/pii/S0950584925000783&hl=en&sa=X&d=1379216563488707466&ei=3tz6Z-HDDvCj6rQPwoSn6A4&scisig=AFWwaeb0mECFrsofCEyewySgPyJO&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=0&folt=rel) |
| LLM, Code | Generation | [Enhancing llm code generation with ensembles: A similarity-based selection approach](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.15838&hl=en&sa=X&d=6315180162277152648&ei=3tz6Z-HDDvCj6rQPwoSn6A4&scisig=AFWwaeYw_s8WAmNdUs0l_UHZtKix&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=1&folt=rel) |
| LLM, Code | Generation | [A Comprehensive Study of LLM Secure Code Generation](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.15554%3F&hl=en&sa=X&d=1363137439941333778&ei=3tz6Z-HDDvCj6rQPwoSn6A4&scisig=AFWwaea70lzbx-2dnx-SlddbyIDc&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=3&folt=rel) |
| LLM, Code, Software Testing |  | [Automated Harmfulness Testing for Code Large Language Models](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.16740&hl=en&sa=X&d=9984898886618882508&ei=3tz6Z-HDDvCj6rQPwoSn6A4&scisig=AFWwaeY9TKp5hroYtjAXp0K1dUfY&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=4&folt=rel) |
| LLM, Code | Repair | [FeedbackEval: A Benchmark for Evaluating Large Language Models in Feedback-Driven Code Repair Tasks](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.06939&hl=en&sa=X&d=3630442079653699433&ei=3tz6Z-HDDvCj6rQPwoSn6A4&scisig=AFWwaeakmawt1RZy7sc-t0c4bk9f&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=5&folt=rel) |
| Code |  | [CKTyper: Enhancing Type Inference for Java Code Snippets by Leveraging Crowdsourcing Knowledge in Stack Overflow](https://scholar.google.com/scholar_url?url=https://seal-queensu.github.io/publications/pdf/FSE-Anji-25.pdf&hl=en&sa=X&d=7004309645188894300&ei=3tz6Z-HDDvCj6rQPwoSn6A4&scisig=AFWwaeYyrjqaFJaDUk1WxX0Qr9lX&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=6&folt=rel) |
| LLM, Code | Generation | [aiXcoder-7B-v2: Training LLMs to Fully Utilize the Long Context in Repository-level Code Completion](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.15301&hl=en&sa=X&d=15788931866516891147&ei=3tz6Z9W1C8uZieoPg4fsmAg&scisig=AFWwaeYi_7K3zAnZWQ5kRBngFmjW&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=1&folt=rel) |
| LLM |  | [Does context matter? contextualjudgebench for evaluating llm-based judges in contextual settings](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.15620&hl=en&sa=X&d=4694277635380098830&ei=3tz6Z9W1C8uZieoPg4fsmAg&scisig=AFWwaeZWWBCgHzhwdV7rV4U7IIiY&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=2&folt=rel) |
| LLM |  | [Dancing with Critiques: Enhancing LLM Reasoning with Stepwise Natural Language Self-Critique](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.17363%3F&hl=en&sa=X&d=11521510970677819720&ei=3tz6Z9W1C8uZieoPg4fsmAg&scisig=AFWwaeZ1FoGj3fIwjgWCbOxO43ev&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=3&folt=rel) |
| LLM |  | [CapArena: Benchmarking and Analyzing Detailed Image Captioning in the LLM Era](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.12329%3F&hl=en&sa=X&d=407472380549964642&ei=3tz6Z9W1C8uZieoPg4fsmAg&scisig=AFWwaeYceA6AtNeTroAmdGm1ugPz&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=4&folt=rel) |
| LLM |  | [Navigating Rifts in Human-LLM Grounding: Study and Benchmark](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.13975&hl=en&sa=X&d=6056628797355529511&ei=3tz6Z9W1C8uZieoPg4fsmAg&scisig=AFWwaeYuzwNKVc6ZCL0NUy7wCU7P&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=5&folt=rel) |
|  | Agent | [SkillWeaver: Web Agents can Self-Improve by Discovering and Honing Skills](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.07079&hl=en&sa=X&d=13301755129364600749&ei=3tz6Z9W1C8uZieoPg4fsmAg&scisig=AFWwaeY7dZcJ4SFWTXTfStwkKDuq&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=6&folt=rel) |
| Software Testing |  | [Task-to-Instance Prompt Learning for Vision-Language Models at Test Time](https://scholar.google.com/scholar_url?url=https://ieeexplore.ieee.org/abstract/document/10925517/&hl=en&sa=X&d=7061085335833209582&ei=3tz6Z9W1C8uZieoPg4fsmAg&scisig=AFWwaeauALB5Xz0dtHolj6VGw3Nk&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=7&folt=rel) |
|  |  | [Auditing language models for hidden objectives](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.10965%3F&hl=en&sa=X&d=1501136133567193109&ei=3tz6Z9W1C8uZieoPg4fsmAg&scisig=AFWwaeadoHBh04I6TvMcoaA7ksCs&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=8&folt=rel) |
|  |  | [Rethinking RL Scaling for Vision Language Models: A Transparent, From-Scratch Framework and Comprehensive Evaluation Scheme](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.02587&hl=en&sa=X&d=3642027329340221236&ei=3tz6Z9W1C8uZieoPg4fsmAg&scisig=AFWwaeb-XYmW-h1bslhyY7wBzqSK&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=9&folt=rel) |
| LLM, Code | Generation | [CCCI: Code Completion with Contextual Information for Complex Data Transfer Tasks Using Large Language Models](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.23231&hl=en&sa=X&d=4201012503536136494&ei=3tz6Z-ySDZuw6rQPjdfcmQQ&scisig=AFWwaeaTwcJgPIAurLq4aX4MyRvJ&oi=scholaralrt&hist=ylyK0_8AAAAJ:16898579961534012346:AFWwaeZADCuvrSiGaZ1pge7b9bMB&html=&pos=2&folt=rel) |
|  |  | [Benchmarking Failures in Tool-Augmented Language Models](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.14227&hl=en&sa=X&d=12864745453246544967&ei=3tz6Z7yNCNSyieoP2ane-QQ&scisig=AFWwaeZOi6uJnH7_v5ou5yMqdUFy&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=3&folt=rel) |
| LLM |  | [How Effectively Do LLMs Extract Feature-Sentiment Pairs from App Reviews?](https://scholar.google.com/scholar_url?url=https://link.springer.com/chapter/10.1007/978-3-031-88531-0_9&hl=en&sa=X&d=16503861718654765605&ei=3tz6Z7yNCNSyieoP2ane-QQ&scisig=AFWwaeYT1ecgB91lHBOvPYNcQzpS&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=5&folt=rel) |
