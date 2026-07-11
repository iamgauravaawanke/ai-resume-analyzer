import { Card, CardContent } from "../components/ui/card";
import { Lightbulb, CheckCircle2 } from "lucide-react";


function SuggestionsCard({ suggestions }) {
  const validSuggestions = suggestions?.filter(
  item => item.trim() !== ""
);

   return (
    <Card className="rounded-3xl border border-slate-200 shadow-md transition-all duration-300 hover:-translate-y-2 hover:shadow-2xl hover:border-blue-300">
      <CardContent className="p-8">

        <div className="flex items-center gap-3">

          <div className="rounded-xl bg-yellow-100 p-3">
            <Lightbulb className="h-6 w-6 text-yellow-600" />
          </div>

          <div>
            <h2 className="text-2xl font-bold text-gray-900">
              Suggestions
            </h2>

            <p className="text-sm text-gray-500">
              Personalized AI recommendations to improve your resume
            </p>
          </div>

        </div>

        <div className="mt-6 space-y-4">

          {validSuggestions?.length > 0 ? (

  validSuggestions.map((item, index) => (

    <div
      key={index}
      className="rounded-2xl border border-slate-200 bg-slate-50 p-5 transition-all duration-300 hover:-translate-y-1 hover:border-blue-300 hover:bg-blue-50 hover:shadow-md"
    >
      <div className="flex items-start gap-3">

        <Lightbulb className="mt-1 h-5 w-5 text-yellow-600" />

        <p className="leading-7 text-gray-700">
          {item}
        </p>

      </div>

    </div>

  ))

) : (

  <div className="rounded-2xl border border-green-200 bg-green-50 p-8 text-center">

    <h3 className="text-xl font-bold text-green-700">
      🎉 Excellent Resume!
    </h3>

    <p className="mt-3 text-gray-600">
      Your resume is already well optimized.
      No additional suggestions are required.
    </p>

  </div>

)}

        </div>

      </CardContent>
    </Card>
  );
}

export default SuggestionsCard;