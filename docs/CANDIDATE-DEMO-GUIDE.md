# CloudBees Senior Solutions Engineer
# Product Demonstration Assessment Guide

---

# Welcome

Congratulations on advancing to the final stage of the interview process.

The next step is a customer-facing product presentation focused on **CloudBees Unify**.

This exercise is designed to simulate a real customer engagement and evaluate how you think and operate as a Solutions Engineer—not whether you're already an expert on CloudBees.

We understand that most candidates have never used CloudBees Unify before. We're intentionally giving you a new product to learn because that's often what Solutions Engineers do.

We're interested in:

* How you learn a new product
* How you prepare
* How you tell a customer story
* How you connect technology to business value
* How you present and answer questions

---

# Your Assignment

Assume you've already completed discovery with a prospective customer.

You are now delivering your first tailored product demonstration.

Your audience includes:

* Engineering Leadership
* Platform Engineering
* DevOps Engineers
* Software Developers
* Enterprise Architects

Expect technical and business questions throughout the presentation.

---

# Presentation Length

**45 Minutes Total**

Recommended format:

| Time      | Topic                      |
| --------- | -------------------------- |
| 5 min     | Customer recap & agenda    |
| 20–25 min | Live Product Demonstration |
| 5–10 min  | Business value summary     |
| 10–15 min | Q&A                        |

---

# Evaluation Criteria

We'll evaluate you on:

* Executive Presence
* Storytelling
* Business Value
* Technical Credibility
* Product Knowledge
* Demo Flow
* Customer Focus
* Handling Questions
* Overall Presentation

We are **NOT** looking for a feature dump.

---

# Customer Scenario

Choose **ONE** of the following customer scenarios.

## Scenario 1 — FinSure Bank

* **Industry:** Financial Services
* **Size:** 20,000 employees · 600+ development teams
* **Toolchain:** GitHub Actions, Jenkins, GitLab CI, Jira, ServiceNow, SonarQube, Artifactory, Azure DevOps, Kubernetes, AWS
* **Problems:** Every business unit uses different CI/CD tools; release managers coordinate releases manually; no single view of delivery; compliance reporting is painful; security approvals vary; leadership lacks visibility; Platform Engineering wants to standardize without forcing migrations.
* **Goals:** Improve governance · increase delivery visibility · reduce release risk · standardize delivery · preserve tool investments · improve developer productivity · enable AI responsibly.

## Scenario 2 — Horizon Health Systems

* **Industry:** Healthcare Technology
* **Size:** 2,500 engineers
* **Toolchain:** GitHub, GitHub Actions, Jenkins, Kubernetes, ArgoCD, Jira, ServiceNow, Terraform, AWS
* **Problems:** Every product team releases differently; developers maintain pipelines manually; approvals inconsistent; leadership has little deployment visibility; AI adoption lacks governance; engineering wants self-service with compliance.
* **Goals:** Standardize delivery · improve developer experience · reduce deployment risk · increase visibility · build reusable Platform Engineering workflows · introduce AI guardrails.

> **Tip:** Pick the scenario you can tell the most convincing story about. FinSure leans **governance / regulated release**; Horizon leans **developer experience / platform golden paths**.

---

# Part 1 — How To Prepare (Suggested 1-Week Plan)

You are **not** expected to master the product. You are expected to prepare like an SE. A workable plan:

| When | Focus |
| --- | --- |
| Day 1 | Create a free CloudBees account. Click through the UI: dashboard, applications, components, workflows, integrations, analytics. Read the "Core Concepts" section below. |
| Day 2 | Fork and connect the two demo repos (below). Run the CI workflow and one release workflow. Watch them execute and view the **Evidence** tab. |
| Day 3 | Watch 2–3 CloudBees Unify product videos (links at the end). Pick your scenario. Draft your story: problem → value → how Unify helps. |
| Day 4 | Build your demo flow. Decide exactly what you'll click, in what order, and the sentence you'll say at each step. Personalize names to your scenario. |
| Day 5 | Dry-run the full 45 minutes out loud. Time it. Prepare answers to the anticipated questions (below). |
| Day 6–7 | Polish. Practice transitions and the executive summary. Have a backup plan if a live step is slow. |

**Golden rule:** every click should map to a business outcome. If you can't say *why it matters*, cut it.

---

# Part 2 — CloudBees Unify: Core Concepts To Understand

You should be comfortable explaining these building blocks in plain language. (Depth beyond this: see the official docs linked at the end — do not over-claim capabilities you haven't verified in your own org.)

### Component
A **component** maps to a source repository and its CI (build/test/scan). One component = one repo. In this kit, the component is `carechart-api`.

### Application
An **application** is a product made up of one or more components. This is where **Release Orchestration** lives. *In CloudBees Unify an application and a component cannot be the same repository* — that's why this kit ships two repos.

### Workflows (Standard vs. Staged)
Workflows are YAML automations stored in `.cloudbees/workflows/`. Two types:
* **Standard** — build/test/deploy automation (e.g. CI).
* **Staged** — organizes a release into ordered **stages** (e.g. Governance → Staging → Prod), typically calling a deployer. The staged designation is expressed with a top-level `metadata: stages/v1alpha1:` block that groups jobs into named stages (the `kind:` stays `workflow`).

### Deployer
A reusable workflow that deploys the components of an application to a target environment, driven by a **manifest**. Staged workflows call the deployer per stage/environment.

### Environments
Deployment targets (e.g. `staging`, `prod`, `qa`) created in the platform and associated with the application. Staged deploy stages map to these.

### Evidence
Each job can publish a **Markdown evidence item** to the run's **Evidence tab** — test results, security findings, approvals, deployment records. This is the backbone of the **governance/auditability** story: "every stage produces evidence automatically."

### Artifacts
A component's CI **registers artifact versions** (e.g. `carechart-api:1.4.x`) with the platform; registered artifacts appear under the component's **Artifacts**. Releases deploy *registered artifact versions* — so CI must register an artifact for a release to have something to deploy. In this kit, `ci.yaml`'s `package` job registers the `carechart-api` artifact.

### Integrations ("Embrace, don't replace")
Unify connects the tools teams already use — GitHub, GitLab, Jenkins, Jira, ServiceNow, Azure DevOps, and more — rather than forcing migration. This is the single most important message in both scenarios.

### Explore in the live UI (not in this repo's YAML)
The following are best shown directly in your trial org; explore them beforehand and speak to them at a business level:
* **Dashboard / unified visibility** — one place to see delivery across tools.
* **Analytics** — deployment metrics, DORA-style insights, executive reporting.
* **Feature Management (feature flags)** — decouple release from deploy; progressive rollout.
* **AI** — assistants, guardrails, and governance (MCP / shared context). Tie this to "enable AI responsibly."

---

# Part 3 — The Demo Kit (Your Starting Building Blocks)

You have two ready-made repositories. They are **self-contained and simulated** — the workflows run green in any CloudBees Unify org with **no real clusters, secrets, or integrations required** — so you can focus on the story, not on infrastructure.

| Repo | Represents | Contents |
| --- | --- | --- |
| **[cloudbees-unify-demo-kit](https://github.com/cb-demos/cloudbees-unify-demo-kit)** | The **Component** (`carechart-api`) | `ci.yaml` (build/test/scan, publishes evidence per job), `deploy.yaml` (simulated component deploy), `k8s/`, `helm/`, and a GitHub Actions CI alternative |
| **[cloudbees-unify-demo-app](https://github.com/cb-demos/cloudbees-unify-demo-app)** | The **Application** (Release Orchestration) | Two **staged** release workflows (FinSure, Horizon), a `deployer.yaml`, plus `manifests/`, `policies/`, `mock-data/` as evidence/talking points |

### What's inside the component repo
* `.cloudbees/workflows/ci.yaml` — `validate → unit-tests → security-scan → package`; **each job publishes an evidence item**, and `package` **registers a build artifact** (`carechart-api` version) so releases have something to deploy.
* `.cloudbees/workflows/deploy.yaml` — simulated component deploy (callable by the deployer, or run standalone); publishes evidence.
* `.github/workflows/ci.yml` — external CI example, to show "keep your existing tools."

### What's inside the application repo
* `.cloudbees/workflows/release-finsure-bank.yaml` — staged: **Governance → Staging → Production Approval → Production → Post-Release**.
* `.cloudbees/workflows/release-horizon-health.yaml` — staged: **Release Readiness → QA → Staging → Post-Release**.
* `.cloudbees/workflows/deployer.yaml` — deploys the component per environment based on the manifest.
* `manifests/`, `policies/`, `mock-data/` — release manifests, governance/approval policies, and mock Jira/ServiceNow/security/evidence data to reference during your talk.

### Setup (do this before the interview)
1. **Fork both repos** into your account/org and **connect them** to your CloudBees Unify trial org.
2. Connect **`cloudbees-unify-demo-kit`** as a **Component**. Open `ci.yaml` and **Run workflow** — confirm it goes green and review the **Evidence tab**.
3. Create the **Application** from **`cloudbees-unify-demo-app`** and **add the component** to it.
4. Create the target **environments** the release workflows use — `staging` + `prod` (FinSure), `qa` + `staging` (Horizon) — and associate them with the application.
5. Run a **release workflow** and walk the stages + Evidence tab.

> **Notes / gotchas:**
> * `deployer.yaml` calls the component's deploy via a cross-repo reference `@main`. If you fork to a different org, update that path.
> * The two release workflows are designated staged via the `metadata: stages/v1alpha1:` block. If your org's composer expects the workflow to be *created* as staged, use **Create staged workflow** and paste/point to the YAML.
> * Everything is **simulated** — no real deployment happens. That's intentional; keep the conversation on outcomes.
> * You can absolutely **extend** these (rename the app/component to your scenario, add a real approval gate in the composer, add feature-flag steps). Tailoring earns points.

---

# Part 4 — Suggested Presentation Flow

### 1. Recap discovery (2–3 min)
> "During discovery we learned your teams use GitHub, Jenkins, GitLab, Azure DevOps, Jira and ServiceNow across many business units. Your biggest challenges are governance, visibility, and coordinating releases without disrupting engineering."

### 2. Establish business value (WHY, before product)
Developer productivity · compliance · faster, safer releases · operational efficiency · engineering consistency · Platform Engineering · AI governance. Don't jump to features yet.

### 3. Position CloudBees Unify
Embrace-not-replace · unified software delivery · visibility · governance · orchestration · AI-ready · Platform Engineering.

### 4. Live demonstration (choose what supports YOUR story)
* **Dashboard** — unified delivery visibility; executive + engineering views.
* **Applications** — application-centric delivery and lifecycle.
* **Workflows** — orchestration: automate manual coordination, connect fragmented tools, standardize. **This is where the kit shines** — run a staged release and show the stages + evidence.
* **Integrations** — how Unify connects existing tools. Reinforce: *customers keep their tools.*
* **AI** (if available) — assistants, guardrails, MCP, governance.
* **Analytics** — deployment metrics, release visibility, executive reporting.

### 5. Wrap up
Summarize problems solved · business outcomes · why CloudBees · suggested next steps.

---

# Part 5 — Sample Demo Script (Adapt Freely)

A concrete 20–25 minute flow using the kit. Personalize names to your scenario.

1. **Frame the pain (1 min).** "You have great tools, but no single view, and releases are coordinated by hand in spreadsheets and email."
2. **Show unified visibility (3–4 min).** Open the Unify **dashboard**; show the application and its components. "One place — leadership and engineers see the same reality."
3. **Show 'embrace not replace' (2–3 min).** Point out the connected tools / the GitHub Actions CI example. "Your teams keep GitHub, Jenkins, Jira. Nothing to rip out."
4. **Run CI (3–4 min).** Trigger `ci.yaml`. As it runs, narrate build → test → security scan → package. Open the **Evidence tab** ("every stage produces audit evidence automatically — no manual compliance packet"), then show the registered artifact under the component's **Artifacts** ("this version is now available for release").
5. **Run the staged release (5–7 min).** Trigger your scenario's release workflow. Walk the **stages** (Governance → Staging → … → Prod). Pause on the **approval** stage: "This is a governed gate — release manager sign-off, captured as evidence." Show the deployer fanning out to the component per environment.
6. **Tell the governance story (2–3 min).** Open the release run's Evidence tab; scroll the per-stage evidence and the mock policy/manifest data. "This is your audit trail — generated by the pipeline, not assembled after the fact."
7. **(Optional) AI / feature flags (2–3 min).** If explored, show AI guardrails or a feature-flag rollout to hit "enable AI safely" / "decouple release from deploy."
8. **Land the value (1–2 min).** Recap: standardized delivery, visibility, governance-without-friction, tools preserved.

> **Backup plan:** live runs can be slow. Have a completed run open in another tab so you can always show finished stages + evidence.

---

# Part 6 — Business Value Mapping (Problem → Capability → Outcome)

Use this to keep every demo moment tied to value.

### FinSure Bank
| Problem | Show in Unify | Business outcome |
| --- | --- | --- |
| Fragmented CI/CD tools | Integrations + GitHub Actions example | Standardize *without* migration; preserve investment |
| Manual release coordination | Staged release workflow + deployer | Faster, repeatable, lower-risk releases |
| Painful compliance reporting | Per-job **Evidence** + policies | Continuous, automated audit trail |
| No leadership visibility | Dashboard + Analytics | Executive insight into delivery |
| Inconsistent security approvals | Governed approval stage | Consistent, enforced controls |

### Horizon Health
| Problem | Show in Unify | Business outcome |
| --- | --- | --- |
| Every team releases differently | Reusable staged workflow ("golden path") | Standardized, self-service delivery |
| Developers hand-maintain pipelines | Reusable workflows + deployer | Better developer experience; less toil |
| Inconsistent approvals | Governed stages + evidence | Compliance without slowing teams |
| Little deployment visibility | Dashboard + Analytics | Engineering + leadership visibility |
| Ungoverned AI adoption | AI guardrails / governance | Introduce AI safely |

---

# Part 7 — Anticipated Questions (Prepare Answers)

**Business / leadership**
* *"Do we have to replace our current tools?"* → No. Unify connects existing tools; embrace-not-replace. Lead with this.
* *"How does this improve compliance?"* → Evidence is produced per stage automatically; approvals are governed gates; audit trail is continuous.
* *"What's the ROI / why now?"* → Less manual coordination, faster safer releases, one source of truth, reduced audit effort.
* *"How disruptive is adoption?"* → Incremental — connect a tool/team at a time; keep existing pipelines.

**Technical / practitioner**
* *"How do workflows differ from GitHub Actions?"* → Similar YAML model; Unify adds orchestration across tools, staged releases, evidence, and cross-repo application/component structure.
* *"Component vs. application?"* → Component = a repo + its CI; application = a product of components with release orchestration (separate repos).
* *"How do approvals work?"* → Manual-approval jobs / gates within a staged workflow; captured as evidence.
* *"Where does deployment actually happen?"* → The deployer calls each component's deploy workflow per environment. *(In this kit it's simulated — say so honestly if asked; the pattern is what matters.)*
* *"How does AI stay governed?"* → Guardrails, shared context/MCP, and policy — point to docs; don't overclaim specifics you haven't verified.

**Handling the unknown (important):** If you don't know, say so and show *how you'd find out*. "Great question — I'd confirm that in the docs / with our product team; here's my understanding…" Honesty + resourcefulness scores better than bluffing.

---

# Part 8 — Common Pitfalls To Avoid

* ❌ **Feature dumping.** Clicking everything with no narrative.
* ❌ **Starting with the product** instead of the customer's problem.
* ❌ **Ignoring the executives** by going too deep too fast (or vice-versa).
* ❌ **Over-claiming.** Don't invent capabilities. "Simulated for this demo" and "I'd verify that" are fine.
* ❌ **No summary.** Always close with problems solved + outcomes + next steps.
* ❌ **Fragile live demo.** Always have a completed run as a backup.

---

# Tips for Success

✅ Start with business challenges · ✅ tell a story · ✅ avoid feature dumping · ✅ explain WHY a feature matters · ✅ personalize the demo · ✅ connect technical capability to business outcome · ✅ keep executives *and* engineers engaged · ✅ end with a compelling summary.

---

# Business Messages That Align With CloudBees

* "Embrace, don't replace."
* "Connect your existing DevOps toolchain."
* "Improve governance without slowing developers."
* "Increase visibility across software delivery."
* "Reduce manual coordination."
* "Standardize delivery across engineering teams."
* "Improve developer experience."
* "Enable Platform Engineering."
* "Introduce AI safely with governance."

---

# Helpful Resources

* **CloudBees:** https://www.cloudbees.com/
* **CloudBees Unify:** https://www.cloudbees.com/products/cloudbees-unify
* **Documentation:** https://docs.cloudbees.com/
* **CloudBees University (free training):** https://university.cloudbees.com/
* **YouTube:** https://www.youtube.com/@CloudBees — search "CloudBees Unify", "CloudBees AI", "Platform Engineering", "Software Delivery"
* **Blog:** https://www.cloudbees.com/blog — Platform Engineering, AI, Software Delivery, Developer Experience, Governance
* **Free trial (hands-on):** https://www.cloudbees.com/free-trial
* **Demo kit — Component:** https://github.com/cb-demos/cloudbees-unify-demo-kit
* **Demo kit — Application:** https://github.com/cb-demos/cloudbees-unify-demo-app

---

# What We Are Really Evaluating

This presentation is **not** about CloudBees. It's about **you**.

If you joined CloudBees, you'd regularly learn new products, build demos, adapt presentations, and explain new capabilities to customers. This exercise lets us see how you approach that.

We look forward to meeting you and wish you the best of luck!
