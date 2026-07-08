import { Card, CardContent } from "../components/ui/card";
import { BarChart3 } from "lucide-react";

function ATSScoreCard({ atsScore }) {

  const getStatus = () => {
    if (atsScore >= 80) return "Excellent";
    if (atsScore >= 60) return "Good";
    return "Needs Improvement";
  };

  const getColor = () => {
    if (atsScore >= 80) return "text-green-600";
    if (atsScore >= 60) return "text-yellow-500";
    return "text-red-500";
  };

  return (
    <Card className="rounded-3xl shadow-lg transition-all duration-300 hover:-translate-y-1 hover:shadow-2xl">

      <CardContent className="flex flex-col items-center p-8">

        <BarChart3 className="h-10 w-10 text-blue-600" />

        <h2 className="mt-3 text-lg font-semibold text-gray-600">
          ATS Score
        </h2>

        <h1 className="mt-4 text-7xl font-extrabold text-blue-600">
          {atsScore}
        </h1>

        <p className={`mt-3 text-lg font-semibold ${getColor()}`}>
          {getStatus()}
        </p>

        <p className="mt-2 text-center text-sm text-gray-500">
          Resume Match Score
        </p>

      </CardContent>

    </Card>
  );
}

export default ATSScoreCard;