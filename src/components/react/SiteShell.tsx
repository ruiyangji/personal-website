import type { ReactNode } from 'react';
import { Theme } from '@astryxdesign/core/theme';
import { neutralTheme } from '@astryxdesign/theme-neutral/built';
import { Button } from '@astryxdesign/core/Button';

const links = [
  ['Home', '/'], ['Projects', '/projects'], ['Experience', '/cv'], ['Writing', '/blog'], ['Life', '/life'],
] as const;

export function SiteHeader({ current = '' }: { current?: string }) {
  return <header className="site-header"><div className="site-header-inner">
    <a className="site-brand" href="/" aria-label="Jerry Ji home"><strong>Jerry Ji</strong><span>Systems × AI × product</span></a>
    <nav className="site-nav" aria-label="Main navigation">{links.map(([label, href]) => <a key={href} href={href} aria-current={current === href ? 'page' : undefined}>{label}</a>)}</nav>
    <div className="header-actions"><Button label="Say hello ↗" variant="secondary" size="sm" href="mailto:rj378@cornell.edu" /></div>
    <details className="mobile-nav"><summary aria-label="Open navigation"/><nav className="mobile-nav-links" aria-label="Mobile navigation">{links.map(([label, href]) => <a key={href} href={href} aria-current={current === href ? 'page' : undefined}>{label}</a>)}<a href="mailto:rj378@cornell.edu">Say hello ↗</a></nav></details>
  </div></header>;
}

export function SiteFooter() {
  return <footer className="site-footer"><span>© {new Date().getFullYear()} Jerry Ji · Built for curious collaborators.</span><a href="mailto:rj378@cornell.edu">rj378@cornell.edu ↗</a></footer>;
}

export function SiteShell({ children, current = '' }: { children: ReactNode; current?: string }) {
  return <Theme theme={neutralTheme} mode="light"><div className="site-frame"><SiteHeader current={current}/><main className="site-main">{children}</main><SiteFooter/></div></Theme>;
}

export function ReadingShell({ children }: { children: ReactNode }) {
  return <Theme theme={neutralTheme} mode="light"><div className="site-frame"><SiteHeader current="/blog"/><main className="site-main site-main--reading">{children}</main><SiteFooter/></div></Theme>;
}
