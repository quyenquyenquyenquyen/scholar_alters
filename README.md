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
|  |  | [Seer: Accelerating Blockchain Transaction Execution by Fine-Grained Branch Prediction](https://scholar.google.com/scholar_url?url=https://www.vldb.org/pvldb/vol18/p822-xiao.pdf&hl=en&sa=X&d=11168060766901762929&ei=ssz2Z4fjDo-j6rQPq-ro-Qg&scisig=AFWwaeaPUcL3LwL9BAYItnVcd0Fp&oi=scholaralrt&hist=ylyK0_8AAAAJ:4974034551180671527:AFWwaebZb4G2z_XAHxtUtGUOv8go&html=&pos=0&folt=cit) |
| LLM, Code | Generation | [A Comprehensive Study of LLM Secure Code Generation](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.15554%3F&hl=en&sa=X&d=1363137439941333778&ei=ssz2Z7-hDZyV6rQPq4Lz0Q4&scisig=AFWwaea70lzbx-2dnx-SlddbyIDc&oi=scholaralrt&hist=ylyK0_8AAAAJ:4812769200119993430:AFWwaeYwgMeQSPpxCfDXmGy5aE3n&html=&pos=0&folt=rel) |
| Vulnerabilities, Smart Contracts, LLM | Detection | [Smart Contract Vulnerability Detection Using Large Language Models and Graph Structural Analysis](https://scholar.google.com/scholar_url?url=https://www.sciencedirect.com/org/science/article/pii/S1546221825002504&hl=en&sa=X&d=4504820058459498391&ei=ssz2Z7-hDZyV6rQPq4Lz0Q4&scisig=AFWwaeZMeaniylWwEGOyOdrF9Ulz&oi=scholaralrt&hist=ylyK0_8AAAAJ:4812769200119993430:AFWwaeYwgMeQSPpxCfDXmGy5aE3n&html=&pos=1&folt=rel) |
| LLM, Code | Generation | [Enhancing High-Quality Code Generation in Large Language Models with Comparative Prefix-Tuning](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.09020&hl=en&sa=X&d=274986171076802173&ei=ssz2Z9HpFMCSieoPxdaHyQM&scisig=AFWwaea-q7yfbqCfb2mRj_yZrJ7q&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=0&folt=rel) |
| LLM, Code | Generation | [Fixing Large Language Models' Specification Misunderstanding for Better Code Generation](https://scholar.google.com/scholar_url?url=https://drive.google.com/file/d/1eiTmCxYs6FgdxCZNOdS9egz6U1Jf4wOL/view&hl=en&sa=X&d=6513233471596826292&ei=ssz2Z9HpFMCSieoPxdaHyQM&scisig=AFWwaeZjNzZZqbOuWO8MZmi5NgiS&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=1&folt=rel) |
| Software Testing | Generation | [KotSuite: Unit Test Generation for Kotlin Programs in Android Applications](https://scholar.google.com/scholar_url?url=https://qixin5.github.io/files/pdf/research/icpc25kotsuite.pdf&hl=en&sa=X&d=4160603672644182246&ei=ssz2Z9HpFMCSieoPxdaHyQM&scisig=AFWwaebk9skrRKkb80KaNdrfD3RV&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=2&folt=rel) |
| Fuzzing |  | [XMutant: XAI-based Fuzzing for Deep Learning Systems](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.07222&hl=en&sa=X&d=13793734475605200419&ei=ssz2Z9HpFMCSieoPxdaHyQM&scisig=AFWwaeYnfys4dbn96t74wYrCxCKf&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=3&folt=rel) |
| Vulnerabilities, LLM | Exploit | [HALURust: Exploiting Hallucinations of Large Language Models to Detect Vulnerabilities in Rust](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.10793&hl=en&sa=X&d=5829414047755650757&ei=ssz2Z9HpFMCSieoPxdaHyQM&scisig=AFWwaeY9qSDL2ktzIVFeZhrU-G2d&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=4&folt=rel) |
| Code |  | [On the compressibility of large-scale source code datasets](https://scholar.google.com/scholar_url?url=https://www.sciencedirect.com/science/article/pii/S0164121225000974&hl=en&sa=X&d=2847125099270029302&ei=ssz2Z9HpFMCSieoPxdaHyQM&scisig=AFWwaeYjHT3aJfr7ec96-PkHPbPL&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=5&folt=rel) |
| Fuzzing, Software Testing |  | [Rocket: A System-Level Fuzz-Testing Framework for the XRPL Consensus Algorithm](https://scholar.google.com/scholar_url?url=https://research.tudelft.nl/en/publications/rocket-a-system-level-fuzz-testing-framework-for-the-xrpl-consens&hl=en&sa=X&d=1494719845448823376&ei=ssz2Z9HpFMCSieoPxdaHyQM&scisig=AFWwaeaP7GjQ1pEEgZqDthdjYWEH&oi=scholaralrt&hist=ylyK0_8AAAAJ:17903213248891513419:AFWwaeaeIo1O_qAhRJzogmnex0DM&html=&pos=6&folt=rel) |
| Vulnerabilities | Detection | [A software vulnerability detection method based on multi-modality with unified processing](https://scholar.google.com/scholar_url?url=https://www.sciencedirect.com/science/article/pii/S0950584925000424&hl=en&sa=X&d=5319209508677612172&ei=ssz2Z5-hEIWlieoPxarRgAo&scisig=AFWwaeZxHxmCJPLJLYUF5XxVdqjT&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=0&folt=rel) |
| Bug |  | [Bug Priority Prediction Using Deep Ensemble Approach](https://scholar.google.com/scholar_url?url=https://www.sciencedirect.com/science/article/pii/S1568494625004090&hl=en&sa=X&d=5946690942891386490&ei=ssz2Z5-hEIWlieoPxarRgAo&scisig=AFWwaeaTWUgoypsuT8nvfYOn5n5-&oi=scholaralrt&hist=ylyK0_8AAAAJ:5865787842749446205:AFWwaeYRVjm7Uk5GklbyG-nM5aLh&html=&pos=1&folt=rel) |
| LLM, Code | Generation | [LLMs Meet Library Evolution: Evaluating Deprecated API Usage in LLM-based Code Completion](https://scholar.google.com/scholar_url?url=https://www.computer.org/csdl/proceedings-article/icse/2025/056900a781/251mHK5tjdC&hl=en&sa=X&d=4291983748355056793&ei=ssz2Z6KAE_Cj6rQPrrHXyQ4&scisig=AFWwaebbFgNB42GTnyK8DsY5wt9u&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=0&folt=rel) |
| LLM |  | [Dapo: An open-source llm reinforcement learning system at scale](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.14476&hl=en&sa=X&d=1968980266662184520&ei=ssz2Z6KAE_Cj6rQPrrHXyQ4&scisig=AFWwaebXNS6d8Y_C8FG4sfvmXe0u&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=1&folt=rel) |
|  |  | [Evolution-based Region Adversarial Prompt Learning for Robustness Enhancement in Vision-Language Models](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.12874&hl=en&sa=X&d=4288320110718600484&ei=ssz2Z6KAE_Cj6rQPrrHXyQ4&scisig=AFWwaebZ47dtXpHPS7gkzptvLmTz&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=2&folt=rel) |
| Vulnerabilities, Verification, LLM | Detection | [Vulnerability Detection: From Formal Verification to Large Language Models and Hybrid Approaches: A Comprehensive Overview](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.10784&hl=en&sa=X&d=12911561823202945144&ei=ssz2Z6KAE_Cj6rQPrrHXyQ4&scisig=AFWwaeYhatByJp-efqzH8QuYSI72&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=3&folt=rel) |
|  | Agent | [AgentDAM: Privacy Leakage Evaluation for Autonomous Web Agents](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.09780%3F&hl=en&sa=X&d=12860650719968363446&ei=ssz2Z6KAE_Cj6rQPrrHXyQ4&scisig=AFWwaeaZP1nOXGDyZqifdZ_WOtaf&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=4&folt=rel) |
| LLM |  | [Aligning Multimodal LLM with Human Preference: A Survey](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.14504&hl=en&sa=X&d=1315835665997175613&ei=ssz2Z6KAE_Cj6rQPrrHXyQ4&scisig=AFWwaeaYxO6Scdjrz2Sdyj1j9_2t&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=5&folt=rel) |
| LLM |  | [LLM Generated Persona is a Promise with a Catch](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.16527&hl=en&sa=X&d=15287455255324878097&ei=ssz2Z6KAE_Cj6rQPrrHXyQ4&scisig=AFWwaeYIlIV_cXUCW5nMHAbkIUyA&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=6&folt=rel) |
| LLM |  | [Temporal Consistency for LLM Reasoning Process Error Identification](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.14495&hl=en&sa=X&d=18020288792776836625&ei=ssz2Z6KAE_Cj6rQPrrHXyQ4&scisig=AFWwaeba3ShxiqHc2VTrBXbMnsjA&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=7&folt=rel) |
|  |  | [Can Large Vision Language Models Read Maps Like a Human?](https://scholar.google.com/scholar_url?url=https://arxiv.org/pdf/2503.14607&hl=en&sa=X&d=17711792295989679905&ei=ssz2Z6KAE_Cj6rQPrrHXyQ4&scisig=AFWwaearFz0gduqYT1JLvxjv6dno&oi=scholaralrt&hist=ylyK0_8AAAAJ:15287030194885030172:AFWwaeaPsVnV5GguxDkLdcyPdvnA&html=&pos=9&folt=rel) |
