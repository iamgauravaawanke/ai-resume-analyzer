import { FileText } from "lucide-react";

function DashboardNavbar() {
  return (
    <nav className="sticky top-0 z-50 border-b bg-white/90 backdrop-blur-md shadow-sm">
      <div className="mx-auto flex h-16 max-w-7xl items-center justify-between px-6">

        {/* Logo */}
        <div className="flex items-center gap-3">
          <div className="rounded-xl bg-blue-600 p-2">
            <FileText className="h-6 w-6 text-white" />
          </div>

          <div>
            <h1 className="text-xl font-bold text-slate-900">
              ResumeAI
            </h1>

            <p className="text-xs text-slate-500">
              AI Resume Analyzer
            </p>
          </div>
        </div>

        {/* Status */}
        <div className="rounded-full bg-green-100 px-4 py-2 text-sm font-medium text-green-700">
          ✅ Analysis Complete
        </div>

      </div>
    </nav>
  );
}

export default DashboardNavbar;