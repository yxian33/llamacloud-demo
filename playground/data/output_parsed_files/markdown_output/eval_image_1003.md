

## Video Compression Network

* Compressing raw video data into a lower-dimensional latent space.

* The latent space is where Sora trains and generates videos, allowing for efficient processing and storage of visual information.

## Spacetime Latent Patches

* Once the video is compressed, it is decomposed into a sequence of spacetime patches.

* The patches are extracted from the compressed video and can represent both spatial and temporal information, making them suitable for images and videos with multiple frames.

## Transformer + Diffusion model

* Sora leverages the scaling properties of transformers, which have shown remarkable performance in various domains, including language modeling and image generation.

* The diffusion transformer architecture allows Sora to effectively scale as a video model, with sample quality improving significantly as training compute increases.

## Language understanding

* Sora uses a highly descriptive captioner model trained on video data.

* This model produces detailed captions that are then used to guide the video generation process, ensuring that the generated videos accurately follow user prompts.

## Emerging Simulation Capabilities

* When trained at scale, Sora exhibits emergent capabilities that allow it to simulate certain aspects of the physical world, such as 3D consistency, object permanence, and interactions with the environment.
