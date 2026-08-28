
import Home from "./pages/Home";
import Results from "./pages/Result";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import  LearningResources from "./pages/LearningResources"
import  InterviewPreparation  from "./pages/InterviewPreparation"

function App() {
  return (
<BrowserRouter>



<Routes>


<Route
path=""
element={<Home/>}  />


<Route
    path="/results/:analysis_id"
element={<Results/>} />



<Route
    path="/result/:analysis_id"
    element={<Results />}
/>

<Route
path="/learning-resources/:analysis_id"
  element={<LearningResources />}
  >

  </Route>

<Route
 
 path="interview-preparation/:role_id"
 element={<InterviewPreparation/>}
>


</Route>



</Routes>


</BrowserRouter>
  );
}

export default App;