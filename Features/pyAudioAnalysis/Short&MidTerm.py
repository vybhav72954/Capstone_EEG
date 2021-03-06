from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import ShortTermFeatures
from pyAudioAnalysis import MidTermFeatures
from glob import glob

#TODO
'''
Add number of Features
Add types of Features
'''

data_dir = "C:/Users/MADHUKAR/Desktop/test/abc/*.wav"
audio_files = glob(data_dir)

for filename in range(0, len(audio_files), 1):
    [Fs, x] = audioBasicIO.read_audio_file(audio_files[filename])
    Mono_Signal = audioBasicIO.stereo_to_mono(x)
    print(Fs)

#short term features
    [Feature, Feature_Names] = ShortTermFeatures.feature_extraction(Mono_Signal, Fs, 0.050 * Fs, 0.025 * Fs, deltas=True)


#mid term features
    [mid_features, short_features, mid_feature_names] = MidTermFeatures.mid_feature_extraction(Mono_Signal, Fs, 1.0 * Fs, 0.75 * Fs, 0.050 * Fs, 0.005 * Fs)
#mid_feature_extraction(signal, sampling_rate, mid_window, mid_step, short_window, short_step)

    print(Feature_Names)
    print(Feature)
    print(mid_feature_names)
    print(mid_features)
