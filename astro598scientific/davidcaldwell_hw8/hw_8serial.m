
tic

[wav_1812,fsOrig1812] = audioread('1812.wav');

BitSecMax = 64000;

fs = 44100;

cCat = [31500 29400 26460 25200 24500 22050 19600 18900 17640 14700 12600 11025 9800 8820 7350 6300 4900];
[N,D] = rat(cCat./fs);

resampleRats = N./D;
freqs = resampleRats.*fsOrig1812;

MaxB = BitSecMax./freqs;

errorVector = zeros(length(cCat),1);
samplingRates = cCat';

timeSerial = toc;

tic

for i = 1:length(N)
    L = N(i);
    M = D(i);
    newFreq = fsOrig1812*L/M;
    filterCut = max(L,M);
    
    rp = 0.1;
    rs = 70;
    wp = 1/filterCut;
    ws = 1.1*wp;
    dev = [(10^(rp/20)-1)/(10^(rp/20)+1)  10^(-rs/20)];
    f = [wp ws];
    a = [1 0];
    
    [n,fo,ao,w] = firpmord(f,a,dev);
    if mod(n,2) ~= 0
        n = n+1;
    end
   
    [b,err,res] = firpm(n,fo,ao,w);
   
    delaySamp = (length(b)-1)/2;
  
   
    upped = upsample(wav_1812,L);
    uppedFilt = L*fftfilt(b,upped);
    downed = downsample(uppedFilt,M);
    

    stdDevQuant = std(downed);
    B = floor(MaxB(i));
    delta = sqrt((2*pi*exp(1)*stdDevQuant^2)/(2^(2*B)));
    quantized = delta*round(downed/delta);
    
    BitSec = B*newFreq;
 
    reUpped = upsample(quantized,M);
    reUppedFilt = M*fftfilt(b,reUpped);
    reDowned = downsample(reUppedFilt,L);

    delayOrig = [zeros((2*delaySamp),1); wav_1812];
    

    error = delayOrig(1:end-2*delaySamp) - reDowned;
    meanErr = mean(error.^2);
    
    errorVector(i) = meanErr;
    
end

timeElapsedParallel = toc;
tic

[sampMin,index] = min(errorVector);
freqMin = samplingRates(index);



format long
outputTotal = [samplingRates'; errorVector'];
filename = sprintf('hw_8outputSerial.txt');
fileID = fopen(filename,'w');
fprintf(fileID,'%6s %12s\r\n','Sampling Rate', 'Calculated Error');
fprintf(fileID,'%6.2f %12.8f\r\n',outputTotal);
fprintf(fileID,'%6s %12.8f\r\n','MinError',sampMin);
fprintf(fileID,'%6s %12.8f\r\n','SampRateMin',freqMin);
fprintf(fileID,'Time Elapsed Parallel %d\r\n',timeElapsedParallel);
timeSerial2 = toc;
timeElapsedSerial = timeSerial + timeSerial2;
fprintf(fileID,'Time Elapsed Serial %d\r\n',timeElapsedSerial);

fclose(fileID);
