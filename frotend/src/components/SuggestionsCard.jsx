import { Card, CardContent } from "../components/ui/card";
import { Lightbulb } from "lucide-react";

function SuggestionsCard({ suggestions }) {
  return (
    <Card className="rounded-3xl shadow-lg transition-all duration-300 hover:-translate-y-1 hover:shadow-2xl">

      <CardContent className="p-8">

        {/* Header */}
        <div className="flex items-center gap-3">

          <div className="rounded-xl bg-yellow-100 p-3">
            <Lightbulb className="h-6 w-6 text-yellow-600" />
          </div>

          <div>
            <h2 className="text-2xl font-bold text-gray-900">
              Suggestions
            </h2>

            <p className="text-sm text-gray-500">
              Personalized AI recommendations
            </p>
          </div>

        </div>

        {/* Suggestions */}
        <div className="mt-6 space-y-4">

          {suggestions.length > 0 ? (
            suggestions.map((item, index) => (
              <div
                key={index}
                className="rounded-2xl border border-slate-200 bg-slate-50 p-5 transition hover:border-blue-300 hover:bg-blue-50"
              >
                <h3 className="font-semibold text-lg text-gray-900">
                  {item.title}
                </h3>

                <p className="mt-2 text-gray-600 leading-7">
                  {item.description}
                </p>
              </div>
            ))
          ) : (
            <p className="font-medium text-green-600">
              🎉 Great! No additional suggestions at the moment.
            </p>
          )}

        </div>

      </CardContent>

    </Card>
  );
}

export default SuggestionsCard;