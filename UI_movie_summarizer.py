import React, { useMemo, useState } from "react";
import {
  LayoutDashboard,
  FileText,
  Settings,
  Search,
  Sparkles,
  Database,
  ClipboardList,
  Menu,
  X,
  Bot,
  ChevronRight,
} from "lucide-react";

type NavItem = {
  label: string;
  icon: React.ReactNode;
  active?: boolean;
};

const navItems: NavItem[] = [
  { label: "Dashboard", icon: <LayoutDashboard className="h-4 w-4" />, active: true },
  { label: "Extract", icon: <Sparkles className="h-4 w-4" /> },
  { label: "Documents", icon: <FileText className="h-4 w-4" /> },
  { label: "Records", icon: <Database className="h-4 w-4" /> },
  { label: "Logs", icon: <ClipboardList className="h-4 w-4" /> },
  { label: "Settings", icon: <Settings className="h-4 w-4" /> },
];

const stats = [
  { label: "Extractions", value: "1,248" },
  { label: "Accuracy", value: "96.4%" },
  { label: "Latency", value: "1.8s" },
  { label: "Schemas", value: "12" },
];

const samples = [
  {
    title: "Movie Summary",
    description: "Extract title, cast, genre, themes, and a concise summary from raw text.",
    tag: "Structured Output",
  },
  {
    title: "Resume Parser",
    description: "Convert a resume into clean fields like skills, experience, and education.",
    tag: "Career Use Case",
  },
  {
    title: "Invoice Reader",
    description: "Pull line items, amounts, dates, and vendor details into a clean format.",
    tag: "Business Automation",
  },
];

function App() {
  const [mobileOpen, setMobileOpen] = useState(false);
  const [query, setQuery] = useState("");

  const filteredSamples = useMemo(() => {
    if (!query.trim()) return samples;
    const q = query.toLowerCase();
    return samples.filter(
      (s) =>
        s.title.toLowerCase().includes(q) ||
        s.description.toLowerCase().includes(q) ||
        s.tag.toLowerCase().includes(q)
    );
  }, [query]);

  return (
    <div className="min-h-screen bg-slate-50 text-slate-900">
      <div className="mx-auto flex min-h-screen w-full max-w-[1600px]">
        <aside className="hidden w-72 shrink-0 border-r border-slate-200 bg-white px-5 py-6 lg:flex lg:flex-col">
          <div className="flex items-center gap-3 border-b border-slate-200 pb-5">
            <div className="flex h-11 w-11 items-center justify-center rounded-2xl bg-slate-900 text-white shadow-sm">
              <Bot className="h-5 w-5" />
            </div>
            <div>
              <p className="text-sm font-semibold tracking-tight">StructExtract-AI</p>
              <p className="text-xs text-slate-500">Architected by Gaurav Singh</p>
            </div>
          </div>

          <nav className="mt-6 space-y-1">
            {navItems.map((item) => (
              <button
                key={item.label}
                className={`flex w-full items-center gap-3 rounded-2xl px-4 py-3 text-left text-sm transition ${
                  item.active
                    ? "bg-slate-900 text-white shadow-sm"
                    : "text-slate-600 hover:bg-slate-100 hover:text-slate-900"
                }`}
              >
                {item.icon}
                <span>{item.label}</span>
              </button>
            ))}
          </nav>

          <div className="mt-auto rounded-3xl bg-slate-900 p-5 text-white shadow-sm">
            <p className="text-sm font-semibold">Production-minded UI</p>
            <p className="mt-2 text-sm text-slate-300">
              Clean layout, accessible controls, and a structured extraction workflow.
            </p>
            <button className="mt-4 inline-flex items-center gap-2 rounded-2xl bg-white px-4 py-2 text-sm font-medium text-slate-900 transition hover:bg-slate-100">
              View pipeline <ChevronRight className="h-4 w-4" />
            </button>
          </div>
        </aside>

        <div className="flex min-h-screen flex-1 flex-col">
          <header className="sticky top-0 z-20 border-b border-slate-200 bg-white/90 backdrop-blur">
            <div className="flex items-center justify-between gap-3 px-4 py-4 sm:px-6 lg:px-8">
              <div className="flex items-center gap-3">
                <button
                  className="inline-flex h-10 w-10 items-center justify-center rounded-2xl border border-slate-200 bg-white lg:hidden"
                  onClick={() => setMobileOpen((v) => !v)}
                  aria-label="Toggle sidebar"
                >
                  {mobileOpen ? <X className="h-5 w-5" /> : <Menu className="h-5 w-5" />}
                </button>
                <div>
                  <h1 className="text-lg font-semibold tracking-tight sm:text-xl">
                    StructExtract-AI
                  </h1>
                  <p className="text-sm text-slate-500">
                    AI-powered structured information extraction
                  </p>
                </div>
              </div>

              <div className="hidden w-full max-w-xl items-center gap-2 rounded-2xl border border-slate-200 bg-slate-50 px-4 py-2 md:flex">
                <Search className="h-4 w-4 text-slate-400" />
                <input
                  value={query}
                  onChange={(e) => setQuery(e.target.value)}
                  placeholder="Search use cases, schemas, or examples..."
                  className="w-full bg-transparent text-sm outline-none placeholder:text-slate-400"
                />
              </div>

              <div className="flex items-center gap-3">
                <div className="rounded-2xl bg-slate-100 px-3 py-2 text-sm font-medium text-slate-700">
                  v1.0
                </div>
              </div>
            </div>
          </header>

          {mobileOpen && (
            <div className="border-b border-slate-200 bg-white px-4 py-4 lg:hidden">
              <nav className="grid gap-2 sm:grid-cols-2">
                {navItems.map((item) => (
                  <button
                    key={item.label}
                    className={`flex items-center gap-3 rounded-2xl px-4 py-3 text-left text-sm transition ${
                      item.active
                        ? "bg-slate-900 text-white"
                        : "border border-slate-200 bg-white text-slate-600"
                    }`}
                  >
                    {item.icon}
                    <span>{item.label}</span>
                  </button>
                ))}
              </nav>
            </div>
          )}

          <main className="flex-1 px-4 py-6 sm:px-6 lg:px-8">
            <section className="grid gap-6 xl:grid-cols-[1.5fr_0.85fr]">
              <div className="space-y-6">
                <div className="rounded-[28px] border border-slate-200 bg-gradient-to-br from-slate-900 to-slate-700 p-6 text-white shadow-sm sm:p-8">
                  <div className="inline-flex items-center gap-2 rounded-full border border-white/15 bg-white/10 px-3 py-1 text-xs font-medium text-slate-100">
                    <Sparkles className="h-3.5 w-3.5" />
                    Structured extraction, made simple
                  </div>
                  <h2 className="mt-4 max-w-2xl text-3xl font-semibold tracking-tight sm:text-4xl">
                    Convert unstructured text into clean, usable data.
                  </h2>
                  <p className="mt-3 max-w-2xl text-sm leading-6 text-slate-300 sm:text-base">
                    Built for movie insights today, but designed like a production system for resumes,
                    invoices, reports, and any document that needs structure.
                  </p>

                  <div className="mt-6 flex flex-wrap gap-3">
                    <button className="rounded-2xl bg-white px-5 py-3 text-sm font-semibold text-slate-900 transition hover:bg-slate-100">
                      Start extraction
                    </button>
                    <button className="rounded-2xl border border-white/20 bg-white/10 px-5 py-3 text-sm font-semibold text-white transition hover:bg-white/15">
                      View schema
                    </button>
                  </div>
                </div>

                <div className="grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
                  {stats.map((item) => (
                    <div key={item.label} className="rounded-3xl border border-slate-200 bg-white p-5 shadow-sm">
                      <p className="text-sm text-slate-500">{item.label}</p>
                      <p className="mt-2 text-2xl font-semibold tracking-tight">{item.value}</p>
                    </div>
                  ))}
                </div>

                <section className="rounded-[28px] border border-slate-200 bg-white p-5 shadow-sm sm:p-6">
                  <div className="flex items-center justify-between gap-3">
                    <div>
                      <h3 className="text-lg font-semibold tracking-tight">Extraction templates</h3>
                      <p className="mt-1 text-sm text-slate-500">
                        Reusable schemas for different real-world document types.
                      </p>
                    </div>
                    <button className="rounded-2xl border border-slate-200 px-4 py-2 text-sm font-medium text-slate-700 transition hover:bg-slate-50">
                      Manage templates
                    </button>
                  </div>

                  <div className="mt-5 grid gap-4 lg:grid-cols-3">
                    {filteredSamples.map((sample) => (
                      <article
                        key={sample.title}
                        className="rounded-3xl border border-slate-200 bg-slate-50 p-5 transition hover:-translate-y-0.5 hover:bg-white hover:shadow-sm"
                      >
                        <span className="inline-flex rounded-full bg-slate-900 px-3 py-1 text-xs font-medium text-white">
                          {sample.tag}
                        </span>
                        <h4 className="mt-4 text-base font-semibold">{sample.title}</h4>
                        <p className="mt-2 text-sm leading-6 text-slate-600">{sample.description}</p>
                      </article>
                    ))}
                  </div>
                </section>
              </div>

              <aside className="space-y-6">
                <section className="rounded-[28px] border border-slate-200 bg-white p-5 shadow-sm sm:p-6">
                  <h3 className="text-lg font-semibold tracking-tight">Project identity</h3>
                  <p className="mt-3 text-sm leading-6 text-slate-600">
                    <span className="font-medium text-slate-900">StructExtract-AI</span> is a clean,
                    structured extraction interface designed to turn raw text into reliable fields and concise summaries.
                  </p>
                  <div className="mt-5 rounded-3xl bg-slate-50 p-4 text-sm text-slate-600">
                    Architected by <span className="font-semibold text-slate-900">Gaurav Singh</span>
                  </div>
                </section>

                <section className="rounded-[28px] border border-slate-200 bg-white p-5 shadow-sm sm:p-6">
                  <h3 className="text-lg font-semibold tracking-tight">Deployment-ready notes</h3>
                  <ul className="mt-4 space-y-3 text-sm text-slate-600">
                    <li className="flex gap-3"><span className="mt-1 h-2 w-2 rounded-full bg-slate-900" />Responsive layout for desktop and mobile.</li>
                    <li className="flex gap-3"><span className="mt-1 h-2 w-2 rounded-full bg-slate-900" />Accessible labels and keyboard-friendly controls.</li>
                    <li className="flex gap-3"><span className="mt-1 h-2 w-2 rounded-full bg-slate-900" />Reusable cards and sections for future expansion.</li>
                  </ul>
                </section>
              </aside>
            </section>
          </main>
        </div>
      </div>
    </div>
  );
}

export default App;
