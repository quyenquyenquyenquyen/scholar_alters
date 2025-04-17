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
| Vulnerabilities |  | [Transfer learning for software vulnerability prediction using Transformer models](https://scholar.google.com/scholar_url?url=https://www.sciencedirect.com/science/article/pii/S0164121225001165&hl=en&sa=X&d=1704083859104944765&ei=FUr_Z-X2F_Cj6rQPwoSn6A4&scisig=AFWwaebqThnUMAyzykWvaSgtXFmK&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=0&folt=rel) |
|  |  | [Automated Assessment in Mobile Programming Courses: Leveraging GitHub Classroom and Flutter for Enhanced Student Outcomes](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2504.04230&hl=en&sa=X&d=4084265759440791903&ei=FUr_Z-X2F_Cj6rQPwoSn6A4&scisig=AFWwaeaqETS3vYteQlWJK9mF3OwV&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=1&folt=rel) |
| LLM, Code |  | [Large Language Models (LLMs) for Source Code Analysis: applications, models and datasets](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.17502&hl=en&sa=X&d=13932223716190867094&ei=FUr_Z_jEIZyV6rQP8q-dkA0&scisig=AFWwaeb1dh07lugR2sszh6eusTe5&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=0&folt=rel) |
| APR, LLM | Repair | [DALO-APR: LLM-based automatic program repair with data augmentation and loss function optimization](https://scholar.google.com/scholar_url?url=https://link.springer.com/article/10.1007/s11227-025-07102-3&hl=en&sa=X&d=10480458481806281342&ei=FUr_Z_jEIZyV6rQP8q-dkA0&scisig=AFWwaeZgISIeIz-af4x6cYmuf3Oy&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=1&folt=rel) |
| LLM, Software Testing | Generation | [Automatic High-Level Test Case Generation using Large Language Models](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.17998&hl=en&sa=X&d=2435370287861060433&ei=FUr_Z_jEIZyV6rQP8q-dkA0&scisig=AFWwaeb0yzfBEwJ9p6RT6YLxQ0vY&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=3&folt=rel) |
| LLM, Code Review, Code |  | [CodeReviewQA: The Code Review Comprehension Assessment for Large Language Models](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.16167&hl=en&sa=X&d=13987149689206803549&ei=FUr_Z_jEIZyV6rQP8q-dkA0&scisig=AFWwaeZRD8EhNW4NSPG4ypaH_WWQ&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=4&folt=rel) |
| LLM, Code | Generation | [Enhancing LLM-based Code Translation in Repository Context via Triple Knowledge-Augmented](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.18305&hl=en&sa=X&d=1496301354611823227&ei=FUr_Z_jEIZyV6rQP8q-dkA0&scisig=AFWwaebZgjNWSGlwwMWRyrQ2cYwe&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=5&folt=rel) |
| LLM, Code | Generation | [ModiGen: A Large Language Model-Based Workflow for Multi-Task Modelica Code Generation](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.18460%3F&hl=en&sa=X&d=9392276640239633917&ei=FUr_Z_jEIZyV6rQP8q-dkA0&scisig=AFWwaeZT_yvBwTF_pGcKhcsdnWzW&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=6&folt=rel) |
| Vulnerabilities, LLM | Detection, Reasoning | [Reasoning with LLMs for Zero-Shot Vulnerability Detection](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.17885&hl=en&sa=X&d=16151102993317123730&ei=FUr_Z-SaFoSlieoPpZSOmAc&scisig=AFWwaeaU1duZG60YHiU0D1fyotku&oi=scholaralrt&hist=ylyK0_8AAAAJ:4812769200119993430:AFWwaeYwgMeQSPpxCfDXmGy5aE3n&html=&pos=0&folt=rel) |
| LLM, Code | Generation | [A Comprehensive Study of LLM Secure Code Generation](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.15554%3F&hl=en&sa=X&d=1363137439941333778&ei=FUr_Z-SaFoSlieoPpZSOmAc&scisig=AFWwaea70lzbx-2dnx-SlddbyIDc&oi=scholaralrt&hist=ylyK0_8AAAAJ:4812769200119993430:AFWwaeYwgMeQSPpxCfDXmGy5aE3n&html=&pos=1&folt=rel) |
| LLM, Code | Agent, Reasoning | [CodeARC: Benchmarking Reasoning Capabilities of LLM Agents for Inductive Program Synthesis](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.23145&hl=en&sa=X&d=7322261732284042571&ei=FUr_Z-SaFoSlieoPpZSOmAc&scisig=AFWwaeaAH4_AfF9MmAImwDIX-Jtw&oi=scholaralrt&hist=ylyK0_8AAAAJ:4812769200119993430:AFWwaeYwgMeQSPpxCfDXmGy5aE3n&html=&pos=2&folt=rel) |
|  |  | [Evolution-based Region Adversarial Prompt Learning for Robustness Enhancement in Vision-Language Models](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.12874&hl=en&sa=X&d=4288320110718600484&ei=FUr_Z_b1G8mpieoPv7aWiQ4&scisig=AFWwaebZ47dtXpHPS7gkzptvLmTz&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=0&folt=rel) |
| LLM |  | [XSShield: Defending Against Stored XSS Attacks Using LLM-Based Semantic Understanding](https://scholar.google.com/scholar_url?url=https://www.mdpi.com/2076-3417/15/6/3348&hl=en&sa=X&d=11849643047241211005&ei=FUr_Z_b1G8mpieoPv7aWiQ4&scisig=AFWwaeZJp-xCesiNk9t9IXhXxSLJ&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=1&folt=rel) |
| LLM |  | [Dapo: An open-source llm reinforcement learning system at scale](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.14476&hl=en&sa=X&d=1968980266662184520&ei=FUr_Z_b1G8mpieoPv7aWiQ4&scisig=AFWwaebXNS6d8Y_C8FG4sfvmXe0u&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=3&folt=rel) |
| Software Testing | Detection | [Test-Time Backdoor Detection for Object Detection Models](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.15293%3F&hl=en&sa=X&d=6052108469819470987&ei=FUr_Z_b1G8mpieoPv7aWiQ4&scisig=AFWwaeZFwCtybcnsCXtBxoexifa2&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=4&folt=rel) |
| LLM | Agent | [Why Do Multi-Agent LLM Systems Fail?](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.13657%3F&hl=en&sa=X&d=6760601859756774675&ei=FUr_Z_b1G8mpieoPv7aWiQ4&scisig=AFWwaeaAVNboT1uLyYYlymPHECf1&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=5&folt=rel) |
| LLM |  | [Aligning Multimodal LLM with Human Preference: A Survey](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.14504&hl=en&sa=X&d=1315835665997175613&ei=FUr_Z_b1G8mpieoPv7aWiQ4&scisig=AFWwaeaYxO6Scdjrz2Sdyj1j9_2t&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=6&folt=rel) |
| LLM |  | [LLM-Based Automation of COSMIC Functional Size Measurement from Use Cases](https://scholar.google.com/scholar_url?url=https://fpalomba.github.io/pdf/Journals/J77.pdf&hl=en&sa=X&d=10857265925413407421&ei=FUr_Z_b1G8mpieoPv7aWiQ4&scisig=AFWwaeYYT0Q2dK2V6Z2SyX7XCGnO&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=7&folt=rel) |
| LLM | Reasoning | [Temporal Consistency for LLM Reasoning Process Error Identification](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.14495&hl=en&sa=X&d=18020288792776836625&ei=FUr_Z_b1G8mpieoPv7aWiQ4&scisig=AFWwaeba3ShxiqHc2VTrBXbMnsjA&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=8&folt=rel) |
| LLM |  | [LLM Generated Persona is a Promise with a Catch](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.16527&hl=en&sa=X&d=15287455255324878097&ei=FUr_Z_b1G8mpieoPv7aWiQ4&scisig=AFWwaeYIlIV_cXUCW5nMHAbkIUyA&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=9&folt=rel) |
