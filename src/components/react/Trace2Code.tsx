import { useEffect, useState } from 'react';
import { Button } from '@astryxdesign/core/Button';
import { Badge } from '@astryxdesign/core/Badge';
import { Card } from '@astryxdesign/core/Card';

type Scenario = { name: string; task: string; actions: string[]; output: string; why: string; metric: string };
const scenarios: Scenario[] = [
  { name: 'Find an overdue invoice', task: 'Open the billing workspace, filter to overdue, and inspect the newest invoice.', actions: ['Open Billing', 'Choose “Overdue” filter', 'Open Northstar Labs invoice', 'Read due date and amount'], output: 'await page.getByRole("link", { name: "Billing" }).click();\nawait page.getByRole("button", { name: "Overdue" }).click();\nawait page.getByRole("row", { name: /Northstar Labs/ }).click();', why: 'A person shows the intended outcome once. The compiler keeps stable intent and drops pointer noise, so the workflow can be replayed and reviewed.', metric: '12 raw events → 4 meaningful steps' },
  { name: 'Update a support ticket', task: 'Find the open ticket from Acme, set priority to high, and assign the on-call owner.', actions: ['Open Support queue', 'Search “Acme”', 'Open matching ticket', 'Set priority to High', 'Assign on-call owner'], output: 'await page.getByRole("link", { name: "Support" }).click();\nawait page.getByRole("searchbox").fill("Acme");\nawait page.getByRole("row", { name: /Acme/ }).click();\nawait page.getByLabel("Priority").selectOption("high");', why: 'A second demonstration helps separate reusable intent from the specific record. Selectors favor accessible roles and labels over fragile screen coordinates.', metric: '18 raw events → 5 meaningful steps' },
];

export default function Trace2Code() {
  const [active, setActive] = useState(0);
  const [playing, setPlaying] = useState(false);
  const [audioStatus, setAudioStatus] = useState('');
  const item = scenarios[active];
  const narration = `Trace2Code turns a demonstrated browser task into reusable automation. In this example, ${item.task} The visual timeline shows the meaningful actions. The generated code uses semantic selectors, which are easier to review and maintain than mouse coordinates.`;
  useEffect(() => () => window.speechSynthesis?.cancel(), []);
  function speak() {
    if (!('speechSynthesis' in window)) { setPlaying(false); setAudioStatus('Speech playback is unavailable in this browser. The complete walkthrough is available in the transcript below.'); return; }
    if (playing) { window.speechSynthesis.cancel(); setPlaying(false); setAudioStatus('Narration stopped. Read the transcript below at any time.'); return; }
    const utterance = new SpeechSynthesisUtterance(narration);
    utterance.onend = () => { setPlaying(false); setAudioStatus('Narration complete.'); };
    utterance.onerror = () => { setPlaying(false); setAudioStatus('Narration could not play. The full transcript is available below.'); };
    window.speechSynthesis.cancel(); window.speechSynthesis.speak(utterance); setPlaying(true); setAudioStatus('Narration is playing.');
  }
  return <section className="trace-section" id="trace2code" aria-labelledby="trace-heading">
    <div className="trace-inner">
      <div className="trace-intro">
        <div><Badge variant="teal" label="INTERACTIVE PROJECT WALKTHROUGH"/><h2 id="trace-heading">Trace2Code</h2><p className="trace-deck">Show a browser workflow once. Turn the demonstration into automation a teammate can inspect, reuse, and adapt.</p></div>
        <div className="trace-why"><span className="eyebrow">WHY IT MATTERS</span><p>Most automation tools ask people to script every step. Trace2Code starts from what a person already knows how to do, then produces understandable Playwright code without an LLM at runtime.</p><a className="text-link" href="/projects#trace2code">See the engineering details ↗</a></div>
      </div>
      <div className="mode-legend" aria-label="Communication modes used in this original walkthrough">
        <div className="mode-legend-item"><strong>VISUAL</strong><span>Action timeline + generated code</span></div><div className="mode-legend-item"><strong>LINGUISTIC</strong><span>Task explanation, labels, code, transcript</span></div><div className="mode-legend-item"><strong>SPATIAL</strong><span>Choose a workflow; follow trace → code → use</span></div><div className="mode-legend-item"><strong>AURAL</strong><span>Optional spoken walkthrough with transcript</span></div>
      </div>
      <div className="trace-workspace">
        <Card className="trace-card trace-flow" padding={6}>
          <div className="trace-card-heading"><div><span className="mode-tag">SPATIAL MODE · CHOOSE A DEMONSTRATION</span><h3>Start with a human task</h3></div><span className="trace-step-count">01 / 03</span></div>
          <div className="scenario-tabs" role="group" aria-label="Choose a sample browser workflow">{scenarios.map((scenario, index) => <button type="button" aria-pressed={active === index} className={active === index ? 'scenario-tab is-active' : 'scenario-tab'} key={scenario.name} onClick={() => setActive(index)}>{scenario.name}</button>)}</div>
          <div id="trace-example" role="region" aria-label={`${item.name} workflow example`}>
          <p className="trace-task">“{item.task}”</p>
          <div className="trace-pipeline"><span className="pipeline-node active"><b>1</b> Demonstrate</span><span className="pipeline-line"/><span className="pipeline-node active"><b>2</b> Distill</span><span className="pipeline-line"/><span className="pipeline-node active"><b>3</b> Reuse</span></div>
          <div className="trace-card-heading trace-subheading"><div><span className="mode-tag">VISUAL MODE · CAPTURED ACTIONS</span><h3>What the compiler keeps</h3></div><Badge variant="success" label={item.metric}/></div>
          <ol className="trace-events">{item.actions.map((action, i) => <li key={action}><span className="event-index">0{i + 1}</span><span>{action}</span><span className="event-type">{i === 0 ? 'NAVIGATION' : i === item.actions.length - 1 ? 'READ' : 'INTERACTION'}</span></li>)}</ol>
          <p className="trace-explanation">{item.why}</p></div>
        </Card>
        <Card className="trace-card trace-output" padding={6}>
          <div className="trace-card-heading"><div><span className="mode-tag">LINGUISTIC MODE · REVIEWABLE OUTPUT</span><h3>Automation someone can own</h3></div><Badge variant="neutral" label="PLAYWRIGHT / TYPESCRIPT"/></div>
          <pre className="trace-code"><code>{item.output}</code></pre>
          <div className="trace-output-note"><span className="output-check">✓</span><p><strong>Why this is useful:</strong> a teammate can read what will happen, change the target data, and run it again. The generated steps use accessible page meaning instead of screen coordinates.</p></div>
          <div className="trace-audio"><div className="trace-card-heading"><div><span className="mode-tag">AURAL MODE · OPTIONAL NARRATION</span><h3>Hear the walkthrough</h3></div><Button label={playing ? 'Stop narration' : 'Play narration'} variant="secondary" size="sm" onClick={speak}/></div><p className="trace-transcript"><strong>Transcript:</strong> {narration}</p><span className="audio-note">Uses your browser’s speech synthesis. Nothing plays automatically.</span><p className="audio-status" aria-live="polite">{audioStatus}</p></div>
        </Card>
      </div>
      <div className="trace-bottom"><p><strong>Designed by Jerry Ji.</strong> The examples are illustrative; the project itself is an original browser automation compiler.</p><a className="trace-link-button" href="/projects#trace2code">Explore Trace2Code ↗</a></div>
    </div>
  </section>;
}
