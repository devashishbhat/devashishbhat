<picture>
  <source media="(max-width: 600px) and (prefers-color-scheme: dark)" srcset="assets/chaiops-hero-mobile-dark.svg">
  <source media="(max-width: 600px) and (prefers-color-scheme: light)" srcset="assets/chaiops-hero-mobile-light.svg">
  <source media="(prefers-color-scheme: dark)" srcset="assets/chaiops-hero-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/chaiops-hero-light.svg">
  <img alt="Devashish Bhat — backend and AI engineer. ChaiOps console showing search relevance improving from 0.61 to 0.84, 100% code-verified citation validity, and restart-safe processing of 50,000 payment records in 20 minutes." src="assets/chaiops-hero-dark.svg" width="100%">
</picture>

<p align="center">
  <strong>Backend systems for when the happy path leaves the building.</strong>
  <br>
  <a href="mailto:dbhat.cs@gmail.com">email</a> ·
  <a href="https://www.linkedin.com/in/devashish-bhat/">linkedin</a> ·
  <a href="assets/resume.pdf">résumé</a>
</p>

### `CURRENT_PROCESS`

Building an LLM recommendation service on AWS Lambda and hybrid marketplace search. Measuring first; hand-waving later.

## `INCIDENT_ARCHIVE`

<a href="https://github.com/devashishbhat/ledger-agent">
  <picture>
    <source media="(max-width: 600px)" srcset="assets/project-ledger-mobile.svg">
    <img src="assets/project-ledger.svg" width="100%" alt="Ledger. Signal: answers sounded right but evidence was optional. System: LangGraph, hybrid search, and code-verified quotes. Result: 100% valid citations and recall at 5 improved from 0.70 to 0.91.">
  </picture>
</a>

<a href="https://github.com/devashishbhat/Jirassic">
  <picture>
    <source media="(max-width: 600px)" srcset="assets/project-jirassic-mobile.svg">
    <img src="assets/project-jirassic.svg" width="100%" alt="Jirassic. Signal: standups ended and action items evaporated. System: Whisper to Gemini to story-pointed Jira tasks. Result: second prize at Hack at Davidson 2025.">
  </picture>
</a>

<a href="https://github.com/devashishbhat/Wmaps">
  <picture>
    <source media="(max-width: 600px)" srcset="assets/project-wmaps-mobile.svg">
    <img src="assets/project-wmaps.svg" width="100%" alt="Wmaps. Signal: the fastest route made for a forgettable drive. System: route-aware discovery, AI stories, and voice. Result: five explore modes with hands-free stories.">
  </picture>
</a>

<details>
<summary><strong>OPEN RUNBOOK // loadout + field logs</strong></summary>
<br>

<p align="center">
  <img src="assets/skills.svg" alt="Java, Go, Python, TypeScript, Spring, FastAPI, Kafka, PostgreSQL, Redis, AWS, Google Cloud, Docker, Kubernetes, and Terraform" width="760">
</p>

```text
PAYMENT RAIL     name verification under 300 ms p95
FAILURE PATH     restart-safe batches; no duplicate debits after recovery
PARALLEL LAB     150+ students mentored across OpenMP, MPI, and CUDA
COMMUNITY MODE   1,000+ members; 14 events; one seven-person crew
```

</details>

<details>
<summary><strong>TRACE LEDGER // how an answer earns its citations</strong></summary>
<br>

```mermaid
flowchart LR
    Question --> Plan
    Plan --> Retrieve
    Retrieve --> Answer
    Answer --> Verify
    Verify -->|supported| Finalize
    Verify -->|unsupported| Retry
    Retry --> Retrieve
    Retry -->|limit reached| Refuse
```

The model handles language. Code checks every quote. If the evidence does not survive verification, the system refuses.

</details>

---

<p align="center">
  <strong>If your backend has an interesting failure mode, bring it.</strong>
  <br>
  I’ll bring the chai. <a href="mailto:dbhat.cs@gmail.com">Start a trace →</a>
</p>
