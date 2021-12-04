#from sklearn.decomposition import PCA
import os
import sys
import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from matplotlib import cm
from sklearn.cluster import AgglomerativeClustering
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt

class CPETool():

    def __init__(
        self, 
        target, 
        answer, 
        group, 
        tsne_comp=2,  
        clustering_method="hierarchical", 
        coordinate_path="", 
        coordinate_name="",
        savemeasure_path="", 
        savemeasure_name="", 
        savefig__path="", 
        savefig_name=f"Kim_GEM_hierarchical_tSNE2_time30.png",
        folder_path="", 
        calculation_target="", 
    ):
        self.target=target
        self.answer=answer
        self.group=group 
        self.clustering_method=clustering_method
        self.tsne_comp=tsne_comp
        
        savemeasure_name=f""
        savefig_path=f"hierarchical/real_plot/"
        savefig_name=f"Kim_GEM_hierarchical_tSNE2_time30.png"
 
        self.folder_path=folder_path, 
        self.clustering_method=clustering_method, 
        self.calculation_target=calculation_target

        if coordinate_path: self.savemeasure_path=savemeasure_path
        else: self.savemeasure_path=f"{self.clustering_method}/measure_text/"

        if coordinate_path: self.savemeasure_path=savemeasure_path
        else: self.savemeasure_path=f"{self.clustering_method}/measure_text/"    

        

    def mkdir(self):
        add_path = ["coordinate", "real_plot", "predicted_plot", "measure_text"]
        for i in add_path:
            path = self.folder_path + self.clustering_method + self.calculation_target + (i, )
            path = "/".join(list(path))
            if not os.path.isdir(path):
                os.makedirs(path)

    def create_label(self):
        real = list(f"real.type {i+1}" for i in range(self.group[0]))
        pred = list(f"pred.type {i+1}" for i in range(self.group[0]))
        return(real, pred)

    def create_colours(self, colormap_used="rainbow"):
        rainbow = cm.get_cmap(colormap_used, self.group[0])
        colormap = rainbow(range(self.group[0]))
        colours = ListedColormap(colormap)
        return colours

    def get_cluster_answer(self): #not finish
        sample_id = []
        sample_types = []
        with open(self.answer, 'r') as fip:
            lines = fip.readlines()[1:]
            for line in lines:
                data = line.strip().split('\t')
                sample_id.append(data[0])
                sample_types.append(data[1])
        sample_id = np.array(sample_id)
        sample_types = np.array(sample_types)
        cluster_answers = sample_types.astype(set)
        categories = a
        return (cluster_answers, categories)

    def convert_colorlabel(self, cluster_answers, categories):
        cluster_answers = np.array(cluster_answers)
        for i in range(len(categories)):
            site = np.where(cluster_answers == categories[i])
            cluster_answers[site] = i
        cluster_answers = list(cluster_answers.astype(int))
        return (cluster_answers)

    def unkown(self):
        ans = {}
        pat_l = 0
        with open(self.answer, mode='r') as t_line:
            tem = t_line.readline().strip('\n').split('\t')
            for n_line in t_line:
                tem = n_line.strip('\n').split('\t')
                if tem[1] not in ans:
                    ans[tem[1]] = set()
                ans[tem[1]].add(tem[0])
                pat_l += 1
        ansl = len(ans)
        anss = sorted(ans)
        return (ansl, anss)

    def get_sample_type_info(self):
        sample_types = []
        with open(self.answer, mode='r') as fip:
            lines = fip.readlines()[1:]
            for line in lines:
                data = line.strip().split('\t')
                sample_types.append(data[1])
        return sample_types

    def get_realanswer_info(self):
        realanswer = {}
        for id, typ in zip(self.sample_id, self.sample_types):
            if typ not in realanswer:
                realanswer[typ] = set()
            else:
                realanswer[typ].add(id)
        realanswer_length = len(realanswer)
        realanswer_keysorted = sorted(realanswer)
        return (realanswer, realanswer_length, realanswer_keysorted) 
    
    def get_sample_info(self):
        value = []
        gene_size = 0
        with open(self.target, mode='r') as fip:
            lines = fip.readlines()
            fst = lines[0]
            data = fst.strip().split('\t')
            sample_id = data[1:]
            sample_size = len(data[1:])
            for line in lines[1:]:
                data = line.strip('\n').split('\t')
                value += data[1:]
                gene_size+=1
        value = np.array(value, dtype=np.float64).reshape(gene_size, sample_size)
        return (value, sample_id)
        
    def run_PCA(self, value):
        value = value.T
        value = PCA(n_components=20).fit_transform(value)
        return value

    def save_measure_info(self):
        # path = 'hierarchical/'+method
        # filename_measurePerTime = file_save+'_measure.txt'
        # fop = open(path+'/'+filename_measurePerTime,'w')
        # fop.write('time\tf-measure\n')
        pass

    def save_realgroup_info(self):
        # filename_tSNE_realGroup = file_save + '_tSNE_realGroup_'+str(t)+'.txt'
        # fop2 = open(path + '/coordinate/' + filename_tSNE_realGroup, 'w')
        # fop2.write('time\tt-SNE_site;group\n')
        #     tSNE_site = []
        # for i in range(len(colors)):
        # 	group = colors[i]
        # 	sample_site = '('+str(value[i,0])+','+str(value[i,1])+');'+str(group)
        # 	tSNE_site.append(sample_site)
        # fop2.write('t'+str(t)+'\t'+'\t'.join(tSNE_site))
        pass

    def save_predictedgroup_info(self):
        # filename_tSNE_predictedGroup = file_save + '_tSNE_predictedGroup_'+str(t)+'.txt'
        # fop3 = open(path + '/coordinate/' + filename_tSNE_predictedGroup, 'w')
        # fop3.write('time\tt-SNE_site;group\n')
        pass
    
    def run_TSNE(self, value):
        tsne = TSNE(n_components=self.tsne_comp[0], perplexity=30, method='exact')
        value = tsne.fit_transform(value)
        return value

    def run_AgglomerativeClustering(self, value):
        value = AgglomerativeClustering(n_clusters=self.group[0], affinity='euclidean', linkage='ward').fit_predict(value)
        value = list(value)
        return value

    def get_predictanswer_info(self, value):
        predictanswer = {} # pre
        for i in range(len(value)):
            sample = 's' + str(i)
            group = value[i]
            if group not in predictanswer:
                predictanswer[group] = set()
            predictanswer[group].add(sample)
        predictanswer_length = len(predictanswer) # prel
        predictanswer_keysorted = sorted(predictanswer) # pres
        return (predictanswer, predictanswer_length, predictanswer_keysorted) 

    def run_fmeasure(self):
        def cal_precision(measure):
            for n1 in self.predictanswer_keysorted:
                for n2 in self.realanswer_keysorted:
                    p = len(self.realanswer[n2] & self.predictanswer[n1]) / len(self.predictanswer[n1])
                    measure['precision'].append(p)
            measure['precision'] = np.array(measure['precision']).reshape(self.predictanswer_length, self.realanswer_length)
            return measure

        def cal_recall(measure):
            for n1 in self.predictanswer_keysorted:
                        for n2 in self.realanswer_keysorted:
                            p = len(self.realanswer[n2] & self.predictanswer[n1]) / len(self.realanswer[n2])
                            measure['recall'].append(p)
            measure['recall'] = np.array(measure['recall']).reshape(self.predictanswer_length, self.realanswer_length)       
            return measure

        def cal_fmeasure(measure):         
            measure['f_measure'] = (2 * measure['precision'] * measure['recall']) / (
                    measure['precision'] + measure['recall'])
            measure['f_measure'][np.isnan(measure['f_measure'])] = 0
            return measure

        def cal_finial_fscore(measure):
            f_score = 0
            mx = np.max(measure['f_measure'], axis=0)
            for n1, n2 in zip(mx, self.realanswer_keysorted):
                f_score += (n1 * len(self.realanswer[n2])) / self.sample_size
            return f_score

        calculation_item = ['precision', 'recall', 'f_measure']
        measure = {}
        for n in calculation_item:
            measure[n] = []
        #print(measure)
        # precision
        measure = cal_precision(measure)
        #print('measure', measure)
        # recall
        measure = cal_recall(measure)
        #print('measure', measure)
        # f_measure
        measure = cal_fmeasure(measure)
        #print('measure', measure)
        f_score = cal_finial_fscore(measure)
        return (f_score, measure)

    def hierarchical_clustering(self):
        self.mkdir()
        value, self.sample_id = self.get_sample_info()
        self.sample_size = value.shape[1]
        self.sample_types = self.get_sample_type_info()
        self.realanswer, self.realanswer_length, self.realanswer_keysorted = self.get_realanswer_info()

        value = self.run_PCA(value)
        value = self.run_TSNE(value)
        self.tsne_coordinate = value   
        
        value = self.run_AgglomerativeClustering(value)
        self.predictanswer, self.predictanswer_length, self.predictanswer_keysorted = self.get_predictanswer_info(value)

        f_score, measure = self.run_fmeasure()

        self.colorlabel = self.convert_colorlabel(self.sample_types, self.realanswer_keysorted) # colors
        self.colours = self.create_colours() # colours
        self.real_label, self.pred_label = self.create_label() #classes,  
        def save_realplot(self, tsne_coordinate):
            fig = plt.figure()
            ax1 = fig.add_subplot(111)
            scatter = ax1.scatter(tsne_coordinate[:, 0], tsne_coordinate[:, 1], s=25, c=self.colorlabel, cmap=self.colours, marker='o', alpha=1)
            legend1 = plt.legend(handles=scatter.legend_elements()[0], labels=self.real_label)
            ax1.set_title(f"{dataset}_{self.calculation_target[0]}_{self.clustering_method[0]}_tSNE{self.tsne_comp} [fmeasure={round(f_score, 6)}]")
            plt.xlabel('t-SNE-1')
            plt.ylabel('t-SNE-2')
            plt.ylim()
            plt.xlim()
            plt.savefig()
            plt.close()
        

        sys.exit()
        
        pass



if __name__ == "__main__":

    path = "./mylabtool/tests/CPETool"
    a = CPETool(
        target=f"{path}/ref/Kim_scRNA_rmZero_log2_feaTop1000.txt", 
        answer=f"{path}/ref/Kim_scRNA_category_table.txt", 
        group=3, 
        folder_path=f"{path}/data", 
        clustering_method="hierarchical", 
        calculation_target="GEM", 
        dataset="Kim",
        
        colormap="",  
        real_label="", 
        predicted_label=""
    )
    a.hierarchical_clustering()