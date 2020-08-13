import React, {PureComponent, useEffect, useState, useContext, useRef} from 'react';
import ReactMapGL, {Source, Layer, Marker} from 'react-map-gl';
import StarRatingComponent from 'react-star-rating-component';

const MAPBOX_TOKEN = 'pk.eyJ1Ijoibm5pc2hhbmtvMyIsImEiOiJjazd2OXF3cGMwNHowM2ZsaHU4dm5hc2dkIn0.8Tr64BIwOIU1CTWKq_BtfQ'; // Set your mapbox token here

class Markers extends PureComponent {
  handleClickMarker = (business) => {
    console.log(business)
    this.props.showDetails(business);
  }
  
  render() {
    const {data} = this.props;
    return data.map( (business, index) => {
      const handler = this.handleClickMarker.bind(this, business);
      return (
        <Marker 
            key={index} 
            longitude={business.longitude} 
            latitude={business.latitude} 
        >
            <div className="imgContiner" onClick={handler}>
              <img src={business.image_url} className="flexibleImg" width="40" height="40"/>
            </div>
        </Marker>
      );
    });
  }
}

const  DetailsPanel = ({details}) => {
  const style = {
    color: 'white',
    background: 'url(' + details.image_url + ') no-repeat center',
  };
  return (
    <div className="details-panel">
      <header className="details-header" style={style}>
      </header>
      <span className="business-name">{details.name}</span>
      <hr/>
      
      <div className="business-name" style={{fontSize: 14}}>
        {details.address}, {details.postal_code}
      </div>
      <div className="business-name stars">
        <StarRatingComponent 
            name="rate1" 
            starCount={5}
            value={details.stars}
        />
        <span style={{fontSize: 14, paddingLeft: 10}}>{`(${details.review_count})`}</span>
      </div>

    </div>
  );
};

const  Map = (props) => {
  const long = -112.0740;
  const lat = 33.4484;

  const [viewport, setViewport] = useState({
    width: 400,
    height: 400,
    latitude: lat,
    longitude: long,
    zoom: 14,
    bearing: 0,
    pitch: 0
  });

  
  const [loading, setLoading] = useState(false);
  const [features, setFeatures] = useState([
    // {name: 'Feature', coordinates: {longitude: -122.4, latitude:37.8}},
    // {name: 'Feature', coordinates: {longitude: -122.4, latitude:37.6}}
  ]);

  const geojson = {
    type: 'FeatureCollection',
    features: features
  };

  async function fetchData() {
    setLoading(true);

    let response = await fetch(`http://localhost:8000/api/restaurant/?type=${props.foodType}`, {
      method: 'GET',
      mode: 'cors'
    });

      // let response1 = await fetch(`http://localhost:8080/search?term=${props.foodType}&latitude=${lat}&longitude=${long}`, {
      //   method: 'GET',
      //   mode: 'cors',
      //   headers: {
      //     'Content-Type': 'application/json',
      //     'Authorization': 'Bearer bMQG1WYBwMkxj27gV2kZGXpQ80VYdvj6bfPjZKcogSFIWNmnftn6l0XZi9j8JcOAhfjyticphZeMLrhkqvcX9A8eb45mIbj41RIxdc4VukcjKM_06l0MfR62BhZvXnYx'
      //   }
      // });
      // const json1 = await response1.json();
      // console.log(json1);

    const json = await response.json();
    console.log(json);
        
    if(json) {
      // setFeatures(json.businesses.map((business) => {
      //   return business;
      // }));
      setFeatures(json.results.map((business) => {
        business.image_url = `http://localhost:8080/yelp_photos/photos/${business.images[0].image_id}.jpg`
        // `https://s3-media4.fl.yelpcdn.com/bphoto/${business.images[0].image_id}/o.jpg`
        return business;
      }));
      
      setLoading(false);
    }
  }
  useEffect(() => {
    if (!!props.foodType) {
      fetchData();
    }
  }, []);

  const mounted = useRef();
  useEffect(() => {
    if (!mounted.current) {
      mounted.current = true;
    } else {
      fetchData();
    }
  }, [props.foodType]);

  const [showDetails, setShowDetails] = useState(false);
  const [details, setDetails] = useState(false);

  const handleShowDetails = details => {
    setShowDetails(true);
    setDetails(details);
  };

  return (
    <React.Fragment>
      {showDetails &&
        <section className="details">
          <DetailsPanel details={details}/>
        </section>
      }
      <ReactMapGL
        {...viewport}
        width="100vw"
        height="100vh"
        mapStyle="mapbox://styles/nnishanko3/ck89q2yn00bnp1imzvgm4nreu"
        onViewportChange={setViewport}
        mapboxApiAccessToken={MAPBOX_TOKEN}
      >
          <Markers data={features} showDetails={handleShowDetails}/>
      </ReactMapGL>
    </React.Fragment>
  );
};

export default Map;
