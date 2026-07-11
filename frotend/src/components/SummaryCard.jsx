import { Card, CardContent } from "../components/ui/card";
import { FileText } from "lucide-react";

function SummaryCard({ summary }) {
  return (
   <Card className="rounded-3xl border border-slate-200 shadow-md transition-all duration-300 hover:-translate-y-2 hover:shadow-2xl hover:border-blue-300">

      <CardContent className="p-8">

        <div className="flex items-center gap-3">
          <div className="rounded-xl bg-blue-100 p-3">
            <FileText className="h-6 w-6 text-blue-600" />
          </div>

          <div>
            <h2 className="text-2xl font-bold text-gray-900">
              Professional Summary
            </h2>

            <p className="text-sm text-gray-500">
              AI generated overview of your resume
            </p>
          </div>
        </div>

        <div className="mt-6 rounded-2xl bg-slate-50 p-6">
          <p className="leading-8 text-gray-700">
            {summary}
          </p>
        </div>

      </CardContent>

    </Card>
  );
}

export default SummaryCard;