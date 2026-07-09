  
    
    
    import { Card, CardContent } from "../components/ui/card";

function LoadingSkeleton() {
  return (
    <div className="space-y-6 animate-pulse">

      {/* Header */}
      <div className="h-28 rounded-3xl bg-slate-200"></div>

      {/* ATS + Summary */}
      <div className="grid grid-cols-1 gap-6 lg:grid-cols-4">

        <Card className="rounded-3xl">
          <CardContent className="p-8">
            <div className="h-40 rounded-xl bg-slate-200"></div>
          </CardContent>
        </Card>

        <Card className="lg:col-span-3 rounded-3xl">
          <CardContent className="p-8">
            <div className="space-y-3">
              <div className="h-6 w-52 rounded bg-slate-200"></div>
              <div className="h-4 rounded bg-slate-200"></div>
              <div className="h-4 rounded bg-slate-200"></div>
              <div className="h-4 w-4/5 rounded bg-slate-200"></div>
            </div>
          </CardContent>
        </Card>

      </div>

      

      {/* Skills */}
      <Card className="rounded-3xl">
        <CardContent className="p-8">
          <div className="space-y-3">
            <div className="h-6 w-48 rounded bg-slate-200"></div>

            <div className="flex flex-wrap gap-3">
              <div className="h-10 w-24 rounded-full bg-slate-200"></div>
              <div className="h-10 w-20 rounded-full bg-slate-200"></div>
              <div className="h-10 w-28 rounded-full bg-slate-200"></div>
              <div className="h-10 w-24 rounded-full bg-slate-200"></div>
            </div>
            </div>
          </CardContent>
        </Card>

    </div>
  );
}

export default LoadingSkeleton;