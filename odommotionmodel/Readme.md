## Inverse Motion model

1. **Translational Distance:**
   ```math
   \Delta trans = \sqrt{(x' - x)^2 + (y' - y)^2}
 

2. **First Rotation (Δrot1):**
   ```math
   \Delta rot1 = \text{atan2}(y' - y, x' - x) - \theta
   ```

3. **Second Rotation (Δrot2):**
   ```math
   \Delta rot2 = \theta' - \theta - \Delta rot1
   ```

## Probability Calculation (Gaussian)

1. **Normal Distribution Probability Density Function:**
   ```math
   p(\mu, \sigma) = \frac{1}{\sqrt{2 \pi \sigma^2}} \exp\left(-\frac{1}{2} \frac{\mu^2}{\sigma^2}\right)
   ```

## Motion Model Probabilities

1. **Probability for Δrot1:**
   ```math
   p_1 = \text{prob}(\Delta rot1_{\text{actual}} - \Delta rot1_{\text{predicted}}, \alpha_1 \cdot |\Delta rot1| + \alpha_2 \cdot |\Delta trans|)
   ```

2. **Probability for Δtrans:**
   ```math
   p_2 = \text{prob}(\Delta trans_{\text{actual}} - \Delta trans_{\text{predicted}}, \alpha_3 \cdot |\Delta trans| + \alpha_4 \cdot (|\Delta rot1| + |\Delta rot2|))
   ```

3. **Probability for Δrot2:**
   ```math
   p_3 = \text{prob}(\Delta rot2_{\text{actual}} - \Delta rot2_{\text{predicted}}, \alpha_1 \cdot |\Delta rot2| + \alpha_2 \cdot |\Delta trans|)
   ```

## Sampling Motion Model


   ```math
   \hat{\Delta rot1} = \Delta rot1 + \frac{1}{2} \sum_{i=1}^{12} \text{rand}(-b, b)
   ```


## New Pose Calculation

1. **New x-coordinate:**
   ```math
   x' = x + \hat{\Delta trans} \cdot \cos(\theta + \hat{\Delta rot1})
   ```

2. **New y-coordinate:**
   ```math
   y' = y + \hat{\Delta trans} \cdot \sin(\theta + \hat{\Delta rot1})
   ```

3. **New Orientation (θ):**
   ```math
   \theta' = \theta + \hat{\Delta rot1} + \hat{\Delta rot2}
   ```
