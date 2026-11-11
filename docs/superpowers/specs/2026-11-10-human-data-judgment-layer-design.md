# Astryx Portfolio and Trace2Code Multimodal Walkthrough

## Intent

Redesign Jerry Ji's full professional website with React 19 and Meta Astryx while preserving Astro's static routes and Netlify deployment. Add an original, interactive Trace2Code walkthrough that explains why turning human browser demonstrations into reusable automation is useful.

## Audience and social action

The site is for startup founders, engineers, product/data teams, and potential collaborators—not only large-company recruiters. It should show how Jerry identifies a practical workflow problem, builds a usable system, and explains its impact. The desired next action is to explore his work or reach out about a project.

## Site goals

- Present a clear professional identity around systems engineering, applied AI, product behavior, and interest in human data.
- Keep Home, Projects, Experience/CV, Writing, Life, individual essays, topic pages, 404, RSS, and sitemap.
- Render site UI with React/Astryx; retain Astro as routing, content, and static generation.
- Preserve project facts, authored essays, résumé PDF, and photos.
- Make the centerpiece useful to visitors unfamiliar with Trace2Code.

## Multimodal piece: Trace2Code

An original interactive project walkthrough demonstrates two sample browser workflows. Visitors switch between an overdue invoice task and a support-ticket task. Each shows meaningful captured actions, the task intent, the emitted Playwright snippet, and a short explanation of the transformation from a demonstrated task to reusable code.

The piece names the benefit plainly: a person can demonstrate an existing workflow; a teammate can inspect, adapt, and rerun the generated automation. Examples are illustrative, while the linked project page and repository describe the actual project.

### Explicit modes

- **Visual:** designed action sequence, event labels, and a formatted code sample.
- **Linguistic:** task descriptions, mode labels, action names, generated code, and a full narration transcript.
- **Spatial:** visitors select between sample workflows and follow a three-stage Demonstrate → Distill → Reuse composition.
- **Aural:** optional click-to-play browser speech synthesis; no autoplay and no audio-only information.

## Design direction

Use a calm, editorial palette with warm paper, ink, teal, and neutral surfaces. Keep identity/navigation compact; use wide readable project layouts and a restrained reading measure for essays. The Trace2Code section pairs task/action flow with generated output and labels all four modes directly. Use Astryx Button, Card, Badge, Theme, and custom CSS for page composition. Maintain keyboard focus, meaningful alt text, readable transcript, reduced motion, and responsive layouts.

## Architecture and constraints

- Astro 5 static output plus React 19 integration and locally bundled Astryx 0.7.13 packages.
- Preserve existing route paths, content collection, blog MDX, RSS, sitemap, assets, and `resume.pdf`.
- Keep Netlify `npm run build`, publish `dist`, and Node 20 configuration.
- Do not use a CDN, iframe, client-side SPA router, real customer data, or interaction analytics.
- The homepage stays server-rendered; only the Trace2Code interface hydrates.
- Include the course-required GAI use disclosure in the final Design Rationale Report, per instructor policy.
