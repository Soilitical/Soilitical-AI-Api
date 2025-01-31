# 🌱 **Soilitical API**

Soilitical's API provides endpoints for interacting with our machine learning model, designed to assist in predicting agricultural outcomes based on various input parameters ( Check how it was built in Notebook directory ). This API is built using Django and offers two main endpoints.

## 🚀 **Endpoints**

### 1. Model Information

- **Endpoint:** `/model-info`
- **Method:** `GET`
- **Description:** Retrieves details about the currently deployed machine learning model, including information such as model classes and configuration.

**Example Request:**

**GET https://apisoilitical.pythonanywhere.com/model-info**

**Example Response:**

```json
{
	"model_info": {
		"model_type": "RandomForestClassifier",
		"n_features": 6,
		"n_estimators": 100,
		"max_depth": 15,
		"feature_importances": [
			0.14326060206149363, 0.18178319059935868, 0.2145381231970259,
			0.11872886382040583, 0.2638537653793756, 0.07783545494234051
		]
	}
}
```

### 2. Make Prediction

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
