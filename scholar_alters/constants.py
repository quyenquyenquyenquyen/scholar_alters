DATA_FOLDER = "./data"
SCOPES = [
    'https://mail.google.com/',
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.modify',
]
CLIENTSECRETS_LOCATION = "./credentials.json"

SOFTWARE_VUL_PATTERN = [
    "Software Vulnerabilities",
    "Vulnerabilities",
    "Vulnerability",
]
SOFTWARE_VERIFY_PATTERN = [
    "Formal Verification",
    "Verification",
]
SMART_CONTRACTS_PATTERN = [
    "Smart Contracts",
]
UNIT_TEST_PATTERN = [
    "Unit Test"
]
APR_PATTERN = [
    "Automated Program Repair",
    "Program Repair",
    "Automated Repair",
]
LLMS_PATTERN = [
    "LLMs",
    "LLM",
    "Language Language Models",
    "Language Language Model",
    "ChatGPT",
    "GPT"
]
FUZZING_PATTERN = [
    "Fuzzing",
    "Fuzz",
]
CODE_REVIEW_PATTERN = [
    "Code Review",
]
CI_PATTERN = [
    "Continuous Integration"
]
FIRST_LEVEL_KEYWORDS = {
    "Vulnerabilities": SOFTWARE_VUL_PATTERN,
    "Verification": SOFTWARE_VERIFY_PATTERN,
    "Smart Contracts": SMART_CONTRACTS_PATTERN,
    "Unit Test": UNIT_TEST_PATTERN,
    "Automated Program Repair": APR_PATTERN,
    "Language Language Models": LLMS_PATTERN,
    "Fuzzing": FUZZING_PATTERN,
    "Code Review": CODE_REVIEW_PATTERN,
    "Continuous Integration": CI_PATTERN,
}

DETECTION_PATTERN = [
    "Detector",
    "Identifying",
    "Detecting",
    "Catching",
    "Detection",
]
REPAIR_PATTERN = [
    "Repair",
    "Repairing",
]
GENERATION_PATTERN = [
    "Generation",
    "Completion",
    "Translation",
]
AGENT_PATTERN = [
    "Agent",
    "Agents",
]
SECOND_LEVEL_KEYWORDS = {
    "Detection": DETECTION_PATTERN,
    "Repair": REPAIR_PATTERN,
    "Generation": GENERATION_PATTERN,
    "Agent": AGENT_PATTERN,
}