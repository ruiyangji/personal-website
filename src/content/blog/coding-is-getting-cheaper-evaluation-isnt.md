---
title: "Coding Is Getting Cheaper. Evaluation Isn't."
description: "As models get faster at execution, the critical engineering problem shifts from producing code to rigorously evaluating, testing, and steering it."
pubDate: "Sep 15 2026"
heroImage: "/post_img.webp"
badge: "AI Systems"
tags: ["AI-Agents", "Evaluation", "Systems", "Infrastructure"]
---

Today, immense energy and capital are poured into developer tools: smarter coding agents, tighter IDE integrations, instant diff generation. Generating code is approaching zero marginal cost.

Yet in production engineering, code generation was rarely the primary bottleneck. The hard part of software has always been knowing whether the system you built actually behaves correctly under real constraints, edge cases, and evolving dependencies.

When generating code becomes trivially cheap, the bottleneck flips completely:

> **The primary engineering challenge is no longer writing the code. It is evaluating, validating, and establishing trust in what was produced.**

---

### The Shallow Proxy Trap

When teams first deploy AI agents into internal workflows, the immediate impulse is to judge them on surface-level metrics:
- Did the model output syntactically valid code?
- Did the unit tests compile?
- Does the PR description sound convincing?

These are **shallow proxies**. In complex distributed infrastructure, a change can pass every local unit test, compile cleanly, and still cause a catastrophic cascading latency spike in production. 

During my time at Meta working on Capacity Efficiency, we dealt with systems responsible for reviewing capacity optimization proposals across thousands of engineers and hundreds of millions of dollars in compute spend. When an agent suggests a capacity reclamation strategy, you cannot rely on an LLM "believing" the idea sounds reasonable.

We built an automated evaluation pipeline called **Chronos** to backtest over 2,000+ historical optimization proposals against ground-truth fleet utilization metrics. That shifted our review adoption from **10% to 70%** across three entire engineering organizations. 

Why? Because trust is built on empirical validation, not conversational confidence.

```
+--------------------------------------------------------------+
|                    The Evaluation Loop                       |
+--------------------------------------------------------------+
|  Proposed Change -> Historical Backtesting -> Fleet Metrics  |
|         ^                                            |       |
|         +---------- Reflection & Refinement <--------+       |
+--------------------------------------------------------------+
```

---

### Hard Questions for the Next Era of AI Infrastructure

If we accept that code generation is largely commoditized, what are the problems worth working on?

1. **How do we construct high-fidelity offline evaluations?**  
   If an agent hallucinates a subtle concurrency flaw, can our evaluation harness catch it before human review?
2. **How do we distinguish demo quality from production resilience?**  
   A demo shows what happens on the happy path. Production engineering tests what happens when network partitions occur, database connections exhaust, or dependencies degrade.
3. **Automated reflection loops:**  
   By adapting techniques like Microsoft's SkillOpt, we gave agents execution workflows that critique their own hypotheses against empirical simulation traces. When the agent fails, the failure itself becomes the prompt for the next hypothesis.
4. **Context boundaries:**  
   How much internal context does an agent actually need? Too little context results in naive suggestions; too much context dilutes attention and inflates latency.

---

### Engineering as Steering

In this new paradigm, our role as engineers looks much more like **steering** than typing:

> The model handles the mechanical execution. The engineer provides the taste, the invariants, the evaluation harnesses, and the organizational context that determines what "correct" actually means.

If you are building in AI today, don't just build another code generator. Build the benchmark, the simulator, the harness, and the truth pipeline. That is where durable advantage lives.
