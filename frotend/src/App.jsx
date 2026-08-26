
import Home from "./pages/Home";
import Results from "./pages/Result";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import  LearningResources from "./pages/LearningResources"

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

</Routes>


</BrowserRouter>
  );
}

export default App;