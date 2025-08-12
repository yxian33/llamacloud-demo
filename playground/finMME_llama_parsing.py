from llama_cloud_services import LlamaParse
import os
import glob
import asyncio
import time

LLAMA_INDEX_KEY = "llx-y0ltTo5HWQzML62BF4cVQYBLq9b0ctutG0ZOVWeB6hLP4VnY"

image_dir = "data/output_images"
parsed_file_dir = "data/output_parsed_files"
os.makedirs(parsed_file_dir, exist_ok=True)

# Get all images
image_files = sorted(glob.glob(f"{image_dir}/*.png"))

# Find already processed images (by .txt file)
parsed_txt_files = set(
    os.path.splitext(os.path.basename(f))[0]
    for f in glob.glob(f"{parsed_file_dir}/*.txt")
)

# Filter images that have not been parsed yet
images_to_parse = [
    f for f in image_files
    if os.path.splitext(os.path.basename(f))[0] not in parsed_txt_files
]

print(f"Found {len(images_to_parse)} images to parse (skipping {len(parsed_txt_files)} already parsed).")
# print(parsed_txt_files)

CONCURRENCY_LIMIT = 10  # Tune this (2-5 is safe for file handles and rate limits)
RETRY_LIMIT = 3

async def parse_image(parser, image_path, semaphore):
    image_file = os.path.basename(image_path).split('.')[0]
    async with semaphore:
        for attempt in range(RETRY_LIMIT):
            try:
                print(f"Parsing image: {image_file} (attempt {attempt+1})")
                result = await parser.aparse(image_path)
                # Save markdown
                md_result_path = f"{parsed_file_dir}/{image_file}.md"
                md_document = await result.aget_markdown()
                with open(md_result_path, "w") as f:
                    f.write(md_document + "\n")
                # Save text
                text_result_path = f"{parsed_file_dir}/{image_file}.txt"
                text_documents = result.get_text_documents()
                with open(text_result_path, "w") as f:
                    for doc in text_documents:
                        f.write(doc.text + "\n")
                print(f"Saved results for image {image_file}")
                return
            except Exception as e:
                print(f"Error parsing {image_file}: {e}")
                if "rate limit" in str(e).lower() or "429" in str(e):
                    wait_time = 2 ** attempt
                    print(f"Rate limited. Retrying in {wait_time} seconds...")
                    await asyncio.sleep(wait_time)
                else:
                    print(f"Non-retryable error for {image_file}. Skipping.")
                    return

async def main():
    parser = LlamaParse(
        api_key=LLAMA_INDEX_KEY,
        num_workers=1
        language="en",
        parse_mode="parse_page_with_agent",
        model="anthropic-sonnet-4.0"
    )
    semaphore = asyncio.Semaphore(CONCURRENCY_LIMIT)
    tasks = [parse_image(parser, image_path, semaphore) for image_path in images_to_parse]
    # Use asyncio.as_completed to process results as they finish
    for future in asyncio.as_completed(tasks):
        await future

if __name__ == "__main__":
    asyncio.run(main())
