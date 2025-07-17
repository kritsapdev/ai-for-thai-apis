# AI for Thai API Gateway

This project demonstrates a two-tier API architecture using Python, Flask, and Docker Compose, leveraging AI for Thai services for text summarization and sentiment analysis.

- **API1 (Summarization & Orchestrator):** Receives user requests, calls AI for Thai Text Summarization, then forwards the summarized text to API2 for sentiment analysis, and finally returns a combined result to the user.
- **API2 (Sentiment Analysis):** Receives text from API1, calls AI for Thai Social Sensing (SSENSE) for sentiment analysis, and returns the result.

Both APIs log their activities to the console, visible via Docker logs.

## Project Structure
ai-for-thai-apis/
├── api1/
│   ├── app.py
│   └── requirements.txt
├── api2/
│   ├── app.py
│   └── requirements.txt
├── .env
├── docker-compose.yml
└── README.md

## Prerequisites

Before you begin, ensure you have the following installed:

-   **Docker Desktop:** Includes Docker Engine and Docker Compose.
    -   [Download Docker Desktop](https://www.docker.com/products/docker-desktop/)
-   **AI for Thai API Keys:** You need an API Key from AI for Thai for both `Text Summarization` and `Social Sensing (SSENSE)` services.
    -   [AI for Thai Services](https://aiforthai.in.th/index.php#services)

## Setup and Deployment

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/ai-for-thai-apis.git](https://github.com/YOUR_USERNAME/ai-for-thai-apis.git) # Replace with your actual repo URL
    cd ai-for-thai-apis
    ```

2.  **Create `.env` file:**
    Create a file named `.env` in the root directory (`ai-for-thai-apis/`) and add your AI for Thai API keys:
    ```env
    AIFORTHAI_SUMMARIZE_API_KEY=YOUR_AIFORTHAI_SUMMARIZE_API_KEY
    AIFORTHAI_SSENSE_API_KEY=YOUR_AIFORTHAI_SSENSE_API_KEY
    ```
    **Important:** Replace `YOUR_AIFORTHAI_SUMMARIZE_API_KEY` and `YOUR_AIFORTHAI_SSENSE_API_KEY` with your actual API keys from AI for Thai.

3.  **Build and Run with Docker Compose:**
    Navigate to the root directory of the project (where `docker-compose.yml` is located) and run the following command:
    ```bash
    docker-compose up --build -d
    ```
    -   `--build`: This flag tells Docker Compose to rebuild the images for `api1` and `api2`. This is necessary the first time you run it or if you make changes to the `app.py` or `requirements.txt` files.
    -   `-d`: This flag runs the services in detached mode (in the background).

    You should see output indicating that the services are being created and started.

## How to Test

Once the services are running, you can test the API using `curl` or any API client (like Postman, Insomnia).

The `api1` service is exposed on port `5000` of your host machine.

1.  **Open your terminal.**

2.  **Send a POST request to API1's `/summarize` endpoint:**

    ```bash
    curl -X POST \
         -H "Content-Type: application/json" \
         -d '{
             "text": "ข้าวเป็นเมล็ดของพืชหญ้า Oryza sativa (ชื่อสามัญ: ข้าวเอเชีย) ที่พบมากในทวีปเอเชีย ข้าวเป็นธัญพืชซึ่งประชากรโลกบริโภคเป็นอาหารสำคัญ โดยเฉพาะอย่างยิ่งในทวีปเอเชีย จากข้อมูลเมื่อปี 2553 ข้าวเป็นธัญพืชซึ่งมีการปลูกมากที่สุดเป็นอันดับสามทั่วโลก รองจากข้าวสาลีและข้าวโพด ข้าวเป็นธัญพืชสำคัญที่สุดในด้านโภชนาการและการได้รับแคลอรีของมนุษย์ เพราะข้าวโพดส่วนใหญ่ปลูกเพื่อจุดประสงค์อื่น มิใช่ให้มนุษย์บริโภค ทั้งนี้ ข้าวคิดเป็นพลังงานกว่าหนึ่งในห้าที่มนุษย์ทั่วโลกบริโภค หลักฐานพันธุศาสตร์แสดงว่าข้าวมาจากการนำมาปลูกเมื่อราว 8,200–13,500 ปีก่อน ในภูมิภาคหุบแม่น้ำจูเจียงของจีน ก่อนหน้านี้ หลักฐานโบราณคดีเสนอว่า ข้าวมีการนำมาปลูกในเขตหุบแม่น้ำแยงซีในจีน ข้าวแพร่กระจายจากเอเชียตะวันออกไปยังเอเชียตะวันออกเฉียงใต้และเอเชียใต้ ข้าวถูกนำมายังทวีปยุโรปผ่านเอเชียตะวันตก และทวีปอเมริกาผ่านการยึดอาณานิคมของยุโรป[3] ปกติการปลูกข้าวเป็นแบบปีต่อปี ทว่าในเขตร้อน ข้าวสามารถมีชีวิตอยู่ได้หลายปีและสามารถไว้ตอ (ratoon) ได้นานถึง 30 ปี ต้นข้าวสามารถโตได้ถึง 1–1.8 เมตร ขึ้นอยู่กับพันธุ์และความอุดมสมบูรณ์ของดินเป็นหลัก มีใบเรียว ยาว 50-100 เซนติเมตร และกว้าง 2-2.5 เซนติเมตร ช่อดอกห้อยยาว 30-50 เซนติเมตร เมล็ดกินได้เป็นผลธัญพืชยาว 5-12 มิลลิเมตร และหนา 2-3 มิลลิเมตร การเตรียมดินสำหรับเพาะปลูกข้าวเหมาะกับประเทศและภูมิภาคที่ค่าแรงต่ำและฝนตกมาก เนื่องจากมันใช้แรงงานมากที่จะเตรียมดินและต้องการน้ำเพียงพอ อย่างไรก็ตาม ข้าวสามารถโตได้เกือบทุกที่ แม้บนเนินชันหรือเขตภูเขาที่ใช้ระบบควบคุมน้ำแบบขั้นบันได แม้ว่าสปีชีส์บุพการีของมันเป็นสิ่งพื้นเมืองของเอเชียและส่วนที่แน่นอนของแอฟริกา ร้อยปีของการค้าขายและการส่งออกทำให้มันสามัญในหลายวัฒนธรรมทั่วโลก วิธีแบบดั้งเดิมสำหรับเตรียมดินสำหรับข้าวคือทำให้น้ำท่วมแปลงชั่วขณะหนึ่งหรือหลังจากการตั้งของต้นกล้าอายุน้อย วิธีเรียบง่ายนี้ต้องการการวางแผนที่แข็งแรงและการให้บริการของเขื่อนและร่องน้ำ แต่ลดพัฒนาการของเมล็ดที่ไม่ค่อยแข็งแรงและวัชพืชที่ไม่มีภาวะเติบโตขณะจมน้ำ และยับยั้งศัตรูพืช ขณะที่การทำให้น้ำท่วมไม่จำเป็นสำหรับการเตรียมดินสำหรับเพาะปลูกข้าว วิธีทั้งหมดในการชลประทานต้องการความพยายามสูงกว่าในการควบคุมวัชพืชและศัตรูพืชระหว่างช่วงเวลาการเจริญเติบโตและวิธีที่แตกต่างสำหรับใส่ปุ๋ยลงดิน"
         }' \
         http://localhost:5000/summarize
    ```

    You should receive a JSON response containing the original text, the summarized text from API1, and the sentiment analysis result from API2.

3.  **View Logs:**
    To see the logs from both API1 and API2, run:
    ```bash
    docker-compose logs -f
    ```
    This will show you the print statements (logs) from both services, demonstrating the flow of requests.

## Stopping the Services

To stop and remove the running Docker containers, networks, and volumes, run:
```bash
docker-compose down