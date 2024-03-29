import React from "react";


const Speed = (props) => {

    const handleSpeedChange = (e) => {
        props.setSelectSpeed(e.target.value)
    }

    return (
        <div className={"speed-container"}>
            <label htmlFor="speed">Playback speed: </label>
            <select onChange={handleSpeedChange} className={"speed"} id={"speed"} value={props.selectSpeed}>
                <option value={0.25}>0.25x</option>
                <option value={0.5}>0.5x</option>
                <option value={0.75}>0.75x</option>
                <option value={1} selected>Normal</option>
                <option value={1.25} >1.25x</option>
                <option value={1.5}>1.5x</option>
                <option value={1.75}>1.75x</option>
                <option value={2}>2x</option>
            </select>
        </div>
    )
}


export default Speed