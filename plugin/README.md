# Caffeinity skills (directory edition)

35 agent skills for Claude Code by Abdul Rahman P Z: writing and content, search
visibility, release checks, research and decisions, careers, outbound and learning. Every skill
is plain Markdown. Nothing in this plugin runs code, installs packages, sends data anywhere or
reads credentials: each skill is instructions and reference notes that Claude reads when the
task matches its description.

This is the subset of the full Caffeinity collection that meets the Claude directory's rules for
plain-Markdown plugins. The full collection, with scripts and workflow agents, is at
[github.com/arm-pz/caffeinity-skills](https://github.com/arm-pz/caffeinity-skills). Each skill has
its own page, source repo and trigger tests at [skillsmith.tech](https://skillsmith.tech/).

## Skills

- **address-findings**: Fixes the CRITICAL and HIGH findings in a consistent-code-review report for one pull request, staying inside the files that PR already changes, then reports each finding as fixed, won't fix (with evidence) or escalate.
- **ai-team-blueprint**: Guide a solo operator or small business from "I want an AI team" to a ready-to-run v1 blueprint for a team of 3 to 5 Claude agents.
- **career-track**: Career positioning and the moves around it: personal brand and function-level visibility, promotion and performance-review narratives, executive presence, salary negotiation scripts, career pivots, networking that reaches opportunities before they are posted, interview preparation for the rooms you are already in, and a plan with immediate actions and ninety-day milestones.
- **check-skill-visibility**: Diagnose why individual agent skill pages are missing from Google Search even when their catalog or homepage appears.
- **choose-effort**: Recommends reasoning effort and an execution mode before heavy work in Claude Code or Codex, with setup instructions and a usage checkpoint.
- **cold-email-list-gate**: Gate a cold-email lead list before it loads: sample ten rows, check company, title, size, and mailbox against the ICP, compare data providers on the same criteria, and return a GO or HOLD decision with the fail pattern and the re-run condition.
- **consistent-code-review**: Perform a deterministic, evidence-backed code review that produces the same findings on re-runs of unchanged code, reconciled against a previous report when one is supplied.
- **crash-test**: Crash-tests a decision before you build it.
- **data-readout**: Raw numbers turned into a decision: dataset interpretation, statistics with the business implication of each finding, chart specifications, pattern and anomaly detection, forecasts built on stated assumptions, segmentation, A/B test significance, dashboard metric selection and report templates, output as an executive summary, findings ranked by impact and the specific actions they support.
- **diagnose-search-visibility**: Diagnose why a website, brand, or service page is missing from Google results or rarely cited in AI search answers.
- **diagnose-usage**: Diagnoses why a completed Codex or Claude Code run used more quota or credits than expected.
- **find-partners**: Finds real, non-competing businesses and publishers that share your audience, such as complementary tools, agencies, newsletters and podcasts, screens out link sellers, picks one collaboration per partner (guest post, expert quote, co-made data, integration listing, podcast) and drafts the ask, written to a partners CSV and one ask file per partner.
- **findable-polish**: Audit content for discoverability gaps with the Findable skill, then generate improved alternatives with Wordsmith.
- **fix-skill-visibility**: Apply and verify evidence-backed fixes for individual agent skill pages missing from Google, using a check-skill-visibility report or equivalent URL-level findings.
- **keyword-guard**: Plan SEO topic clusters and eliminate keyword cannibalization so exactly one page wins each query.
- **keyword-resolver**: Resolve keyword cannibalization with Keyword-Guard, then generate alternative titles/H1/meta descriptions with Wordsmith.
- **platform-content**: Platform-native content packs: Twitter/X threads, LinkedIn posts, YouTube and TikTok scripts, Instagram captions, newsletter issues, blog articles, podcast outlines, 30-day calendars and repurposing chains, each with hook, body and call to action, built from a brief about your platform, niche, audience and goal.
- **pre-ship-performance-audit**: Audit and fix real-world web app performance before launch using four independent read-only subagent audits covering images and fonts, frontend bundles and rendering, database queries and APIs, and server, network and user-flow measurement.
- **production-code**: Production-ready code delivered as a complete artifact: scripts, bug fixes with the root cause, API integrations, SQL of any complexity, automation jobs, scrapers, data analysis in pandas or R, technical documentation and architecture write-ups, each with setup steps, error handling and a plain-English explanation of every section.
- **recruiter-lens**: Review resumes, CVs, cover letters and LinkedIn profiles the way recruiters commonly screen them, and prepare candidates for interviews.
- **research-brief**: Decision-grade research: topic overviews, competitor and industry analysis, literature reviews, fact checks with conflicting sources flagged, synthesis of expert positions, trend scans, due diligence on a partner or investment, interpretation of numbers found in public sources and one-page executive briefs, with every claim tied to a dated source read in the session and unknowns named instead of filled in.
- **sales-copy**: Direct-response conversion assets: long-form sales pages, launch and abandoned-cart email sequences, Facebook, Google and LinkedIn ad variations, landing pages, product descriptions, video sales letter and webinar scripts, upsell flows and testimonial frameworks, each with headline, subheadline, body and call to action, built from the product, the buyer, their awareness level and the conversion goal.
- **seo-polish**: Audit SEO health with seo-crawl (and seo-audit when installed), then generate optimized alternatives with Wordsmith.
- **setup-claude-advisor**: Configure persistent advisor and subagent model tiers in Claude Code or local Codex.
- **skill-estate**: Takes a whole collection of agent skill repos from scattered to published, consistent and self-maintaining, in gated phases: inventory every repo, reconcile site, marketplace and README listings, test and tune the family, close workflow gaps, wire publishing so new skill repos go live on their own, bundle a plugin with agents, add trigger tests and directory listings, and leave a maintenance loop and a map.
- **skill-launch**: Launch a new skill end-to-end.
- **solo-income-blueprint**: Design a realistic one-person online income plan from the user's skills, time and budget: one recommended business model, one offer, a demand check, a content and sales path, automations, a minimal tool stack, and a 7-day launch plan.
- **strategy-memo**: Business strategy written as a decision document: competitive analysis, market and customer research, business model canvas, growth and pricing strategy, go-to-market plan, SWOT ranked by actionability, ninety-day, one-year and three-year roadmaps, board presentations and pivot assessments, structured as situation analysis, recommendation and execution roadmap.
- **study-system**: A personal system for acquiring a skill: decomposition into the minimum viable components, a beginner-to-practitioner roadmap, the mental models that unlock a subject, Feynman-level explanations, deliberate-practice routines, knowledge-gap audits that surface wrong assumptions, spaced-repetition schedules, application exercises and honest mastery assessments of where the learner actually is.
- **topic-primer**: Use when the user names a topic and wants to be taught it — from absolute zero, step by step, concept by concept, through a full beginner-to-expert curriculum, with a personal tutor that diagnoses and adapts, in how experts think and which mental models to use, in avoiding common beginner mistakes, tested by a strict examiner, or explained in ultra-simple terms (ELI5).
- **tune-and-polish**: Tune a skill's trigger and boundaries with Tune-Skill and then polish its discoverability with Findable-Polish, in one pass.
- **upstream-polish**: Audit upstream drift and listing mismatches with upstream-check, then generate polished fixes with Wordsmith.
- **verify-search-visibility**: Measure what changed after a website's SEO or AI search fixes go live.
- **web-preflight**: Use when shipping, deploying, publishing, launching, reviewing, or pre-flighting a website or API and you want a lightweight check for accidental exposure of secrets, source or configuration files, admin and debug surfaces, unsafe redirects, missing security controls, and misleading 200 responses.
- **wordsmith**: Write, draft, rewrite, edit, proofread, polish and improve text while preserving the author's intended meaning, facts and voice.

## Privacy

This plugin collects, stores and sends no data. It contains only Markdown instructions: no
scripts, hooks or MCP servers, no network calls, no credentials and no third-party services. The
skills work only on what you give Claude in your conversation, which Claude handles under its own
terms; the plugin adds no data flow of its own. Questions:
[open an issue](https://github.com/arm-pz/caffeinity-directory/issues).

## License

MIT. See LICENSE.
