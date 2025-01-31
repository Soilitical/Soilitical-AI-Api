# 🌱 **Soilitical API**

Soilitical's API provides an endpoint for interacting with our machine learning model, designed to assist in predicting agricultural outcomes based on various input parameters. This API is built using Django and offers one main endpoint.

## 🚀 **Endpoint**

### Make Prediction

- **Endpoint:** `/predict`
- **Method:** `POST`
- **Description:** Takes input data to make a prediction using the machine learning model. Returns the predicted class label.

**Request Format:**

**_Headers:_**

```http
Content-Type: application/json
```

### Example Request: POST https://apisoilitical.pythonanywhere.com/predict

# **Body:**

```json
{
	"soil_type": "clayey soil - loamy soil",
	"ec_value": 0.97,
	"temperature": 23.0,
	"n_value": 23.85,
	"p_value": 15.61,
	"k_value": 20.49
}
```

### Example Response:

```json
{
	"prediction": "Mangoes"
}
```

## **Postman Example:**

![Prediction](image.png)
