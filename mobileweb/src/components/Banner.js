import React from "react";
import { Carousel } from "react-bootstrap";


const Banner = (props) => {
    return (
        <Carousel.Item>
            <img className="d-block w-100" src={props.obj.image} alt={props.obj.name} />
        </Carousel.Item>
    )
}

export default Banner