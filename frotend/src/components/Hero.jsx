import { Button } from "../components/ui/button";

function Hero() {
  return (
    <section className="py-24">
      <div className="container mx-auto flex flex-col items-center px-6 text-center">

        {/* AI Badge */}
        <span className="rounded-full bg-blue-100 px-5 py-2 text-sm font-semibold text-blue-600 shadow-sm">
          🚀 AI Powered Resume Analysis
        </span>

        {/* Heading */}
        <h1 className="mt-8 max-w-5xl text-5xl font-extrabold leading-tight tracking-tight text-gray-900 md:text-6xl">
          Build a Resume That{" "}
          <span className="text-blue-600">
            Gets Interview Calls
          </span>
        </h1>

        {/* Description */}
        <p className="mt-6 max-w-3xl text-lg leading-8 text-gray-600">
          Upload your resume and receive an ATS score, AI-generated summary,
          technical skills analysis, missing skills, and personalized
          recommendations to improve your chances of getting hired.
        </p>

        {/* Feature Badges */}
        <div className="mt-8 flex flex-wrap justify-center gap-4">
          <div className="rounded-full bg-white px-5 py-2 text-sm font-medium shadow-md">
            ✅ ATS Score
          </div>

          <div className="rounded-full bg-white px-5 py-2 text-sm font-medium shadow-md">
            🤖 AI Analysis
          </div>

          <div className="rounded-full bg-white px-5 py-2 text-sm font-medium shadow-md">
            📄 PDF Upload
          </div>

          <div className="rounded-full bg-white px-5 py-2 text-sm font-medium shadow-md">
            💡 Personalized Suggestions
          </div>
        </div>

        {/* Action Buttons */}
        <div className="mt-10 flex flex-wrap justify-center gap-4">

          <Button
            size="lg"
            className="rounded-xl bg-blue-600 px-8 py-6 text-lg font-semibold hover:bg-blue-700"
          >
            Analyze Resume
          </Button>

          <Button
            variant="outline"
            size="lg"
            className="rounded-xl border-blue-600 px-8 py-6 text-lg text-blue-600 hover:bg-blue-50"
          >
            Learn More
          </Button>

        </div>

      </div>
    </section>
  );
}

export default Hero;