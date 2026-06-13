import gaussiansmooth as gs

x, orig, noisy = gs.generate_noisy_data()
smooth = gs.gaussian_smooth(noisy, 20)

gs.plot_smoothing(x, orig, noisy, smooth)