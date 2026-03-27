# Made by 6810110354 Supphakit Cheawmon

นายศุภกิตติ์ เชี่ยวหมอน

# Python Concurrency Lab

A comprehensive demonstration of three concurrency approaches in Python: threading, asyncio, and process pools. Each example showcases best practices and typical use cases.

## Project Overview

This project demonstrates three distinct concurrency models:
- **Threading**: Lightweight concurrency for I/O-bound operations
- **Asyncio**: Async/await concurrency for I/O-bound operations
- **Process Pool**: True parallelism for CPU-bound operations

## Project Structure

```
.
├── thread_example/
│   └── download_thread.py      # Threading for concurrent downloads
├── asyncio_example/
│   └── async_fetch.py          # Asyncio for concurrent API calls
├── process_pool_example/
│   └── cpu_process_pool.py     # ProcessPoolExecutor for CPU-bound work
└── README.md
```

## Running the Examples

### Thread Example
Simulates downloading multiple files concurrently using threads:

```bash
python thread_example/download_thread.py
```

**Output example:**
```
[THREAD] Starting download: file1.pdf
[THREAD] Starting download: file2.zip
[THREAD] Starting download: file3.tar.gz
[THREAD] Starting download: file4.iso
[THREAD] Completed download: file2.zip
[THREAD] Completed download: file3.tar.gz
[THREAD] Completed download: file1.pdf
[THREAD] Completed download: file4.iso

All downloads completed in 2.XX seconds
```

### Asyncio Example
Simulates fetching data from multiple APIs concurrently:

```bash
python asyncio_example/async_fetch.py
```

**Output example:**
```
[ASYNCIO] Starting fetch: API_1
[ASYNCIO] Starting fetch: API_2
[ASYNCIO] Starting fetch: API_3
[ASYNCIO] Starting fetch: API_4
[ASYNCIO] Completed fetch: API_3
[ASYNCIO] Completed fetch: API_1
[ASYNCIO] Completed fetch: API_4
[ASYNCIO] Completed fetch: API_2

All fetches completed in 2.XX seconds
Results: ['Data from API_1', 'Data from API_2', 'Data from API_3', 'Data from API_4']
```

### Process Pool Example
Calculates large factorials in parallel across multiple CPU cores:

```bash
python process_pool_example/cpu_process_pool.py
```

**Output example:**
```
Starting process pool CPU-bound calculations...

Factorial calculations completed in X.XX seconds
factorial(5000) = 42391... (last 10 digits: 1622400000)
factorial(6000) = 12522... (last 10 digits: 3040000000)
...
```

## Threading vs Asyncio vs Process Pool

### Threading
- **Best for**: I/O-bound operations (network requests, file I/O, database queries)
- **Overhead**: Low, lightweight
- **Scalability**: Good for hundreds of concurrent tasks
- **Complexity**: Simple to understand and implement
- **Limitation**: Subject to Python's Global Interpreter Lock (GIL) for CPU-bound work

**Use when:**
- Doing multiple I/O operations that would block otherwise
- Operating on different files or network connections
- Need simple synchronous-like code

### Asyncio
- **Best for**: I/O-bound operations with many concurrent tasks
- **Overhead**: Very low, single-threaded
- **Scalability**: Excellent for thousands of concurrent tasks
- **Complexity**: Requires understanding of async/await
- **Advantage**: No GIL limitations, more efficient for massive concurrency

**Use when:**
- Need to handle thousands of concurrent I/O operations
- Building web servers, websocket handlers, or message brokers
- Want maximum efficiency with single-threaded event loop

### Process Pool
- **Best for**: CPU-bound operations
- **Overhead**: High, separate Python processes
- **Scalability**: Limited by number of CPU cores
- **Complexity**: Data serialization overhead, isolated memory
- **Advantage**: Bypasses GIL, true parallelism

**Use when:**
- Performing heavy computation (parsing, calculations, data processing)
- Need to fully utilize multi-core systems
- Task duration is long enough to overcome process creation overhead

## Key Differences

| Feature | Threading | Asyncio | Process Pool |
|---------|-----------|---------|-------------|
| I/O-Bound | ✓ Best | ✓ Best | ✗ Overkill |
| CPU-Bound | ✗ GIL limits | ✗ GIL limits | ✓ Best |
| Ease of Use | ✓ Simple | ~ Moderate | ~ Moderate |
| Scalability | Good (100s) | Excellent (1000s) | Limited (cores) |
| Memory per Task | ~1-2 MB | ~50 KB | ~50 MB |
| Context Switching | OS level | Single thread | Process level |

## Requirements

- Python 3.7+
- Standard library only (no external dependencies)

## Notes

- Thread example demonstrates concurrent I/O with simulated network delays
- Asyncio example shows efficient handling of multiple concurrent operations
- Process pool example calculates large factorials to simulate CPU-intensive work
- All examples include timing to demonstrate concurrency benefits

---

# Python Concurrency Lab

การสาธิตอย่างละเอียดเกี่ยวกับสามวิธีการของความพร้อมกัน (Concurrency) ใน Python: Threading, Asyncio, และ Process Pools โดยแต่ละตัวอย่างแสดงให้เห็นแนวทางปฏิบัติที่ดีและกรณีการใช้งานทั่วไป

## ภาพรวมของโครงการ

โปรเจกต์นี้สาธิตโมเดลความพร้อมกันทั้งสามแบบ:
- **Threading**: ความพร้อมกันเบาน้อยสำหรับการดำเนินการที่ผูกติด I/O
- **Asyncio**: ความพร้อมกันแบบ async/await สำหรับการดำเนินการที่ผูกติด I/O
- **Process Pool**: การประมวลผลแบบขนาน (Parallelism) จริงสำหรับการดำเนินการที่ผูกติด CPU

## โครงสร้างโครงการ

```
.
├── thread_example/
│   └── download_thread.py      # Threading สำหรับการดาวน์โหลดพร้อมกัน
├── asyncio_example/
│   └── async_fetch.py          # Asyncio สำหรับเรียก API พร้อมกัน
├── process_pool_example/
│   └── cpu_process_pool.py     # ProcessPoolExecutor สำหรับงาน CPU
└── README.md
```

## วิธีการรันตัวอย่าง

### ตัวอย่าง Thread
จำลองการดาวน์โหลดไฟล์หลายๆ ไฟล์พร้อมกันโดยใช้เธรด:

```bash
python thread_example/download_thread.py
```

### ตัวอย่าง Asyncio
จำลองการดึงข้อมูลจาก API หลายแหล่งพร้อมกัน:

```bash
python asyncio_example/async_fetch.py
```

### ตัวอย่าง Process Pool
คำนวณแฟกทอเรียลขนาดใหญ่แบบขนานบนหลาย CPU cores:

```bash
python process_pool_example/cpu_process_pool.py
```

## Threading vs Asyncio vs Process Pool

### Threading
- **เหมาะสมสำหรับ**: การดำเนินการที่ผูกติด I/O (เรียก API, อ่านไฟล์, query ฐานข้อมูล)
- **ค่าใช้สอย**: ต่ำ, เบาน้อย
- **ความสามารถในการขยาย**: ดีสำหรับ 100+ งานพร้อมกัน
- **ความซับซ้อน**: ง่ายต่อการเข้าใจและใช้งาน
- **ข้อจำกัด**: ได้รับผลกระทบจาก Global Interpreter Lock (GIL) สำหรับงาน CPU-bound

**ใช้เมื่อ:**
- ทำหลายๆ การดำเนินการ I/O ที่จะทำให้โปรแกรมค้าง
- ทำงานกับไฟล์หรือการเชื่อมต่อเครือข่ายที่แตกต่างกัน
- ต้องการโค้ดแบบ synchronous ที่เรียบง่าย

### Asyncio
- **เหมาะสมสำหรับ**: การดำเนินการที่ผูกติด I/O ที่มีงานพร้อมกันมากมาย
- **ค่าใช้สอย**: น้อยมาก, เธรดเดี่ยว
- **ความสามารถในการขยาย**: ยอดเยี่ยมสำหรับ 1000+ งานพร้อมกัน
- **ความซับซ้อน**: ต้องเข้าใจ async/await
- **ข้อดี**: ไม่มีข้อจำกัด GIL, มีประสิทธิภาพมากสำหรับความพร้อมกันในขนาดใหญ่

**ใช้เมื่อ:**
- ต้องการจัดการ 1000+ การดำเนินการ I/O พร้อมกัน
- สร้าง web servers, websocket handlers, หรือ message brokers
- ต้องการประสิทธิภาพสูงสุดด้วย event loop เดี่ยว

### Process Pool
- **เหมาะสมสำหรับ**: การดำเนินการที่ผูกติด CPU
- **ค่าใช้สอย**: สูง, กระบวนการ Python แยกต่างหาก
- **ความสามารถในการขยาย**: จำกัดด้วยจำนวน CPU cores
- **ความซับซ้อน**: การ serialize ข้อมูล, หน่วยความจำแยกต่างหาก
- **ข้อดี**: บายพาส GIL, true parallelism

**ใช้เมื่อ:**
- ทำการคำนวณหนัก (parsing, calculations, data processing)
- ต้องใช้ประโยชน์จาก multi-core systems อย่างเต็มที่
- ระยะเวลาของงานนานพอเพื่อให้เหนือกว่าต้นทุนการสร้าง process

## ความแตกต่างหลัก

| คุณสมบัติ | Threading | Asyncio | Process Pool |
|---------|-----------|---------|-------------|
| I/O-Bound | ✓ ดีที่สุด | ✓ ดีที่สุด | ✗ ใช้มากเกินไป |
| CPU-Bound | ✗ GIL limits | ✗ GIL limits | ✓ ดีที่สุด |
| ความง่าย | ✓ ง่าย | ~ ปานกลาง | ~ ปานกลาง |
| ความสามารถขยาย | ดี (100s) | ยอดเยี่ยม (1000s) | จำกัด (cores) |
| หน่วยความจำต่องาน | ~1-2 MB | ~50 KB | ~50 MB |
| Context Switching | OS level | Single thread | Process level |

## ข้อกำหนด

- Python 3.7+
- Standard library เท่านั้น (ไม่มี external dependencies)

## หมายเหตุ

- ตัวอย่าง Thread แสดงให้เห็น concurrent I/O ด้วยการจำลองความล่าช้าของเครือข่าย
- ตัวอย่าง Asyncio แสดงการจัดการการดำเนินการ I/O พร้อมกันหลายรายการอย่างมีประสิทธิภาพ
- ตัวอย่าง Process Pool คำนวณแฟกทอเรียลขนาดใหญ่เพื่อจำลองงานที่ผูกติด CPU
- ตัวอย่างทั้งหมดรวมเวลาเพื่อแสดงให้เห็นถึงประโยชน์ของความพร้อมกัน
