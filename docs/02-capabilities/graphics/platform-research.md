# Graphics and presentation platform research

**Status:** Research evidence; contracts and ADRs hold normative conclusions.

## Windows: Direct3D and DXGI

DXGI swap-chain presentation distinguishes synchronization interval and flags, can report occlusion, device reset/removal, and supports dirty rectangles through newer presentation paths. Flip-model guidance recommends bounding frames in flight because successful `Present` calls may otherwise queue CPU work and inflate latency. A presented buffer may be unbound/reused, so ownership transitions are explicit.

Primary sources: [`IDXGISwapChain::Present`](https://learn.microsoft.com/en-us/windows/win32/api/dxgi/nf-dxgi-idxgiswapchain-present), [DXGI flip model](https://learn.microsoft.com/en-us/windows/win32/direct3ddxgi/dxgi-flip-model), [Direct3D 12 swap chains](https://learn.microsoft.com/en-us/windows/win32/direct3d12/swap-chains), [device removed handling](https://learn.microsoft.com/en-us/windows/uwp/gaming/handling-device-lost-scenarios).

## Linux: Vulkan WSI

Vulkan exposes explicit devices, queues, memory, synchronization, surface capabilities, image acquisition, and queue presentation. `VK_SUBOPTIMAL_KHR`, `VK_ERROR_OUT_OF_DATE_KHR`, `VK_ERROR_SURFACE_LOST_KHR`, and `VK_ERROR_DEVICE_LOST` distinguish recoverable surface evolution from device failure. External synchronization rules demonstrate that thread safety is object/operation specific, not a blanket API property.

Primary sources: [Vulkan specification](https://registry.khronos.org/vulkan/specs/latest/html/vkspec.html), [`VK_KHR_swapchain`](https://registry.khronos.org/vulkan/specs/latest/man/html/VK_KHR_swapchain.html), [`vkAcquireNextImageKHR`](https://registry.khronos.org/vulkan/specs/latest/man/html/vkAcquireNextImageKHR.html), [`vkQueuePresentKHR`](https://registry.khronos.org/vulkan/specs/latest/man/html/vkQueuePresentKHR.html).

The portable contract does not require Vulkan on Linux. OpenGL/EGL, software, and remote providers remain possible when they prove the same selected workload contract and quality claims.

## macOS: Metal and Core Animation

`CAMetalLayer` maintains a bounded drawable pool. `nextDrawable()` can wait and return no drawable; Apple recommends acquiring late and releasing promptly to avoid stalls. Presentation is scheduled with a command buffer after render work. Drawable availability, command completion, and presentation therefore remain separate milestones.

Primary sources: [`CAMetalLayer`](https://developer.apple.com/documentation/quartzcore/cametallayer), [`nextDrawable()`](https://developer.apple.com/documentation/quartzcore/cametallayer/nextdrawable()), [onscreen presentation](https://developer.apple.com/documentation/metal/onscreen-presentation), [`MTLCommandBuffer.present`](https://developer.apple.com/documentation/metal/mtlcommandbuffer/present(_:)).

## Derived portability conclusions

| Native variance | Portable rule |
|---|---|
| Feature/limit models differ | Negotiate exact workload vector |
| Swap-chain/drawable acquisition may block | Async acquisition with deadline and bounded leases |
| Present return does not prove visibility | Separate submission, acceptance, display milestones |
| Surface/device changes invalidate objects | Generation/epoch-scoped resources and explicit recreation |
| Queue models differ | Explicit dependencies; minimal portable ordering |
| Software fallback exists | New provider resolution with disclosed quality |

