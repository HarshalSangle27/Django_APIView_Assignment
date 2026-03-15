# Modular Entity and Mapping System API

This project is a modular backend built with Django and Django REST Framework. It manages master entities (Vendors, Products, Courses, Certifications) and their mappings using strictly `APIView` based endpoints and `drf-yasg` for documentation.

## Installed Apps
[cite_start]As per the strict modularity requirements, this project contains 7 separate Django apps[cite: 260]:

**Master Apps:**
* `vendor`
* `product`
* `course`
* `certification`

**Mapping Apps:**
* `vendor_product_mapping`
* `product_course_mapping`
* `course_certification_mapping`

## Setup Steps
[cite_start]Follow these steps to get the project running on your local machine[cite: 259]:

1. **Clone the repository:**
   ```bash
   git clone <your-github-repo-url>
   cd <repository-folder>