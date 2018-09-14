
import glob 
import pandas as pd
#files= glob.glob("*events.tsv") //puts TSV files in list 


files = glob.glob('*events.tsv')  # grab onsets for each run
def large_small(files):
    # true_outfile= open("HC_01_LReward.txt", 'w')
    # false_outfile= open("HC_02_SReward.txt", 'w')
    for line in files:
        events= pd.read_csv(line, sep='\t') # read in the tsv files
        ## if the choice includes the number 20, extract the time for this stimuli 
        ### into a file called HC_01_LReward
        for event, onset_time in zip (events.Outcome, events.onset):
            if (event == 20):
                with open("HC_01_LReward.txt", 'w') as true_outfile:
                    true_outfile.write(str(onset_time))
            elif (event ==1):
                with open("HC_02_SReward.txt", 'w') as false_outfile:
                    false_outfile.write(str(onset_time))
    true_outfile.close()
    false_outfile.close()

def framing_nf(files):
    for line in files:
        events= pd.read_csv(line, sep='\t') 
        for event, e, f in zip(events.finalDecision, events.onset, events.Frame):
            ##event is the risky or non risky option
           ##e = onset time
            if ((f == "Loss" and event == "B") or (f == "Gain" and event == "A" )):
                with open ("HC_01_Framing", 'w') as frame_outfile:
                    frame_outfile.write(str(e))
            else:
                with open ("HC_02_NoFraming", 'w') as nf_outfile:
                    nf_outfile.write(str(e))


def gist_framing_nf(files):
    for line in files:
        events= pd.read_csv(line, sep='\t') 
        for event, onset_time, frame_cond , fuzzy in zip(events.finalDecision, events.onset, events.Frame, events.FTT):
            ##event is the risky or non risky option
            if ((frame_cond == "Loss" and event == "B") or (frame_cond== "Gain" and event == "A") and fuzzy == "Gist" ):
                with open ("HC_01_GNoFraming", 'w') as frame_outfile:
                    frame_outfile.write(str(onset_time))
            else:
                with open ("HC_02_GFraming", 'w') as nf_outfile:
                    nf_outfile.write(str(onset_time))

def verbatim_framing_nf(files):
    for line in files:
        events= pd.read_csv(line, sep='\t') 
        for event, onset_time, frame_cond , fuzzy in zip(events.finalDecision, events.onset, events.Frame, events.FTT):
            ##event is the risky or non risky option
            if ((frame_cond == "Loss" and event == "B") or (frame_cond== "Gain" and event == "A") and fuzzy == "Verbatim" ):
                with open ("HC_01_VNoFraming", 'w') as frame_outfile:
                    frame_outfile.write(str(onset_time))
            else:
                with open ("HC_02_VFraming", 'w') as nf_outfile:
                    nf_outfile.write(str(onset_time))


def framing_small_lg(files):
    for line in files:
        events= pd.read_csv(line, sep='\t') 
        for event, e, f, out  in zip(events.finalDecision, events.onset, events.Frame, events.Outcome):
            ##event is the risky or non risky option
           ##e = onset time
            if ((f == "Loss" and event == "B") or (f== "Gain" and event == "A") and out == 1 ):
                with open ("HC_01_SmallFraming", 'w') as small_frame_outfile:
                    small_frame_outfile.write(str(e))
            elif ((f == "Loss" and event == "B") or (f== "Gain" and event == "A") and out == 20):
                with open ("HC_02_LargeFraming", 'w') as nf_outfile:
                    nf_outfile.write(str(e))

def gist_verbatim(files):
    for line in files:
        events= pd.read_csv(line, sep='\t')
        for event, onset_time in zip (events.FTT, events.onset):
            if (event == "Gist"):
                with open("HC_02_GFraming.txt", 'w') as gist_outfile:
                    gist_outfile.write(str(onset_time))
            elif (event == "Verbatim"):
                with open("HC_02_Verbatim.txt", 'w') as verbatim_outfile:
                    verbatim_outfile.write(str(onset_time))

def gistGainSure(files):
     for line in files:
        events= pd.read_csv(line, sep='\t')
        for event, onset_time , frame, fuzzy in zip(events.finalDecision, events.onset, events.Frame, events.FTT):        
            if (event == "A" and frame =="Gain" and fuzzy =="Gist" ):
                with open("HC_01_GGSure.txt", 'w') as gist_gain_outfile:
                    gist_gain_outfile.write(str(onset_time))
            elif (event =="B" and frame =="Gain" and fuzzy == "Gist"):
                with open("HC_02_GGRisk.txt", 'w') as gist_risk_outfile:
                    gist_risk_outfile.write(str(onset_time))


def gistLossRisk(files):
     for line in files:
        events= pd.read_csv(line, sep='\t')
        for event, onset_time , frame, fuzzy in zip(events.finalDecision, events.onset, events.Frame, events.FTT):        
            if (event == "B" and frame =="Loss" and fuzzy =="Gist" ):
                with open("HC_01_GLRisk.txt", 'w') as gain_risk_outfile:
                    gain_risk_outfile.write(str(onset_time))
            elif (event =="A" and frame =="Gain" and fuzzy == "Verbatim"):
                with open("HC_02_GLSure.txt", 'w') as gain_sure_outfile:
                    gain_sure_outfile.write(str(onset_time))



def verbatimGainRisk(files):
     for line in files:
        events= pd.read_csv(line, sep='\t')
        for event, onset_time , frame, fuzzy in zip(events.finalDecision, events.onset, events.Frame, events.FTT):        
            if (event == "B" and frame =="Gain" and fuzzy =="Verbatim" ):
                with open("HC_01_VGRisk.txt", 'w') as gain_risk_outfile:
                    gain_risk_outfile.write(str(onset_time))
            elif (event =="A" and frame =="Gain" and fuzzy == "Verbatim"):
                with open("HC_02_VGSure.txt", 'w') as gain_sure_outfile:
                    gain_sure_outfile.write(str(onset_time))


def verbatimLossSure(files):
     for line in files:
        events= pd.read_csv(line, sep='\t')
        for event, onset_time , frame, fuzzy in zip(events.finalDecision, events.onset, events.Frame, events.FTT):        
            if (event == "A" and frame =="Loss" and fuzzy =="Verbatim" ):
                with open("HC_01_VLSure.txt", 'w') as vl_outfile:
                    vl_outfile.write(str(onset_time))
            elif (event =="B" and frame =="Loss" and fuzzy == "Verbatim"):
                with open("HC_02_VLRisk.txt", 'w') as vl_risk_outfile:
                    vl_risk_outfile.write(str(onset_time))

def risk_sure(files):
    for line in files:
        events= pd.read_csv(line, sep='\t')
        for event, onset_time in zip(events.finalDecision, events.onset):
            if (event == "B"):
                with open("HC_02_Risk.txt", 'w') as risk_outfile:
                    risk_outfile.write(str(onset_time))
            elif (event =="A"):
                with open("HC_02_Sure.txt", 'w') as sure_outfile:
                    sure_outfile.write(str(onset_time))

def gain_risk_sure(files):
    for line in files:
        events= pd.read_csv(line, sep='\t')
        for event, onset_time , frame in zip(events.finalDecision, events.onset, events.Frame):        
            if (event == "B" and frame =="Gain"):
                with open("HC_01_GainRisk.txt", 'w') as gain_risk_outfile:
                    gain_risk_outfile.write(str(onset_time))
            elif (event =="A" and frame =="Gain"):
                with open("HC_02_GainSure.txt", 'w') as gain_sure_outfile:
                    gain_sure_outfile.write(str(onset_time))

def loss_risk_sure(files):
    for line in files:
        events= pd.read_csv(line, sep='\t')
        for event, onset_time , frame in zip(events.finalDecision, events.onset, events.Frame):
            if (event == "B" and frame =="Loss"):
                with open("HC_01_LossRisk.txt", 'w') as loss_risk_outfile:
                    loss_risk_outfile.write(str(onset_time))
            elif (event =="A" and frame =="Loss"):
                with open("HC_02_LossSure.txt", 'w') as loss_sure_outfile:
                    loss_sure_outfile.write(str(onset_time))

def gain_loss(files):
    for line in files:
        events= pd.read_csv(line, sep='\t')
        for event, onset_time in zip(events.Frame, events.onset):
            if (event == "Gain"):
                with open ("HC_01_Gain.txt", 'w') as gain_outfile:
                    gain_outfile.write(str(onset_time))
            else:
                with open("HC_02_Loss.txt", 'w') as loss_outfile:
                    loss_outfile.write(str(onset_time))

def gainSmall(files):
    for line in files:
        events= pd.read_csv(line, sep='\t')
        for event, onset_time, frame_cond in zip(events.Outcome, events.onset, events.Frame ):
            if (event == 1 and frame_cond == "Gain"):
                with open ("HC_01_SmallGain.txt", 'w') as gainsm_outfile:
                    gainsm_outfile.write(str(onset_time))
            elif (event == 20 and frame_cond == "Gain") :
                with open("HC_02_LargeGain.txt", 'w') as gainlg_outfile:
                    gainlg_outfile.write(str(onset_time))

            
def lossSmall(files):
    for line in files:
        events= pd.read_csv(line, sep='\t')
        for event, onset_time, frame_cond in zip(events.Outcome, events.onset, events.Frame ):
            if (event == 1 and frame_cond == "Loss"):
                with open ("HC_01_SmallLoss.txt", 'w') as loss_sm_outfile:
                    loss_sm_outfile.write(str(onset_time))
            elif (event == 20 and frame_cond == "Loss") :
                with open("HC_02_LargeLoss.txt", 'w') as loss_lg_outfile:
                    loss_lg_outfile.write(str(onset_time))

def sureSmall(files):
    for line in files:
        events= pd.read_csv(line, sep='\t')
        for event, onset_time, desc in zip(events.Outcome, events.onset, events.finalDecision ):
            if (event == 1 and desc == "A"):
                with open ("HC_01_SmallSure.txt", 'w') as sm_sure_outfile:
                    sm_sure_outfile.write(str(onset_time))
            elif (event == 20 and desc == "A") :
                with open("HC_02_LargeSure.txt", 'w') as lg_sure_outfile:
                    lg_sure_outfile.write(str(onset_time))

def riskSmall(files):
    for line in files:
        events= pd.read_csv(line, sep='\t')
        for event, onset_time, desc in zip(events.Outcome, events.onset, events.finalDecision ):
            if (event == 1 and desc == "B"):
                with open ("HC_01_SmallRisk.txt", 'w') as sm_risk_outfile:
                    sm_risk_outfile.write(str(onset_time))
            elif (event == 20 and desc == "B") :
                with open("HC_02_LargeRisk.txt", 'w') as lg_risk_outfile:
                    lg_risk_outfile.write(str(onset_time))