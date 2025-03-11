export default function LandmarkCard({landmarksLength, landmarkName, landmarkDescription, landmarkIndex, landmarkChangeIndex, buttonColor, btnFunction}) {
    const btnClass = "py-2 px-4 rounded " + buttonColor;
    
    function handleNext(){
        landmarkChangeIndex((landmarkIndex + 1) % landmarksLength)
    }

    function handlePrevious(){
        landmarkChangeIndex((landmarkIndex - 1 + landmarksLength) % landmarksLength)
    }

    return <div className="flex flex-col justify-evenly items-center p-4 space-y-4 w-full h-[35%] bg-white rounded-3xl">
        <h2 className="bold text-3xl">{landmarkName}</h2>
        <p>{landmarkDescription}</p>
        <button onClick={btnFunction} className={btnClass}>Find landmark</button>
        <div className="flex justify-evenly w-full">
            <button onClick={handlePrevious} className="bg-blue-400 p-2 rounded-md xl:w-[30%]">Previous</button>
            <button onClick={handleNext} className="bg-blue-400 p-2 rounded-md xl:w-[30%]">Next</button>
        </div>
    </div>


}