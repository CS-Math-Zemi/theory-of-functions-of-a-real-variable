# -*- coding: utf-8 -*-
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# ==========================================
# 【設定】理系レポート用スタイル設定 (Academic Style)
# ==========================================
def setup_academic_style():
    """
    matplotlibのパラメータを論文・レポート品質に設定する関数
    """
    # 1. LaTeXフォント設定
    plt.rcParams['text.usetex'] = True
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = ['Times New Roman', 'Computer Modern Roman']
    
    # 2. 目盛りの設定 (内向き)
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.rcParams['xtick.top'] = True
    plt.rcParams['ytick.right'] = True
    
    # 3. フォントサイズ (基本設定)
    plt.rcParams['font.size'] = 12
    plt.rcParams['axes.labelsize'] = 14
    plt.rcParams['legend.fontsize'] = 12
    
    # 4. レイアウト
    plt.rcParams['figure.figsize'] = [6.4, 4.8]
    plt.rcParams['axes.grid'] = False

    print("Loaded academic style settings.")

# ==========================================
# 【作図】サンプルプロット処理 (幾何学図形)
# ==========================================
def main():
    # スタイルの適用
    setup_academic_style()
    
    # --- ユーザー指定のサンプル描画コード ---
    
    # 図の全体サイズをかなり大きく設定 (幅24インチ, 高さ10インチ)
    fig, axes = plt.subplots(1, 3, figsize=(24, 10))

    # 共通の設定パラメータ
    radius = 1.0
    center = (0, 0)
    arrow_start = (0.2, 0)  # 矢印の始点
    arrow_end = (0.9, 0)    # 矢印の終点

    # カラー設定
    fill_color = '#a0cbe2'
    edge_color = 'black'
    text_color = 'black'
    hole_color = 'white'

    # フォントサイズ設定 (図形用に特大サイズ)
    math_fontsize = 40
    label_fontsize = 30

    # 各図のパラメータ設定
    # (キャプションの数式, 塗りつぶし有無, 線のスタイル)
    configs = [
        (r'$\Delta^{*}(z_0, R)$', True, '--'),        # 穴あき開円板
        (r'$\bar{\Delta}^{*}(z_0, R)$', True, '-'),   # 穴あき閉円板
        (r'$\partial\Delta(z_0, R)$', False, '-')     # 境界
    ]

    for ax, (label, fill, style) in zip(axes, configs):
        # 1. 大きな円の描画
        circle = patches.Circle(
            center, 
            radius, 
            facecolor=fill_color if fill else 'none', 
            edgecolor=edge_color, 
            linestyle=style, 
            linewidth=4,
            alpha=0.6 if fill else 1.0
        )
        ax.add_patch(circle)
        
        # --- 注釈の描画 ---

        # 2. 半径 R の矢印とラベル
        ax.annotate(
            '', xy=arrow_end, xytext=arrow_start,
            arrowprops=dict(arrowstyle='<->', color='black', lw=3), zorder=20
        )
        ax.text((arrow_start[0] + arrow_end[0])/2, -0.2, r'$R$', 
                ha='center', va='top', fontsize=label_fontsize, color=text_color, zorder=20)
        
        # 3. 中心点 z0 の穴（白抜き丸）の描画
        ax.scatter(*center, 
                   facecolor=hole_color, 
                   edgecolor='black', 
                   s=250,
                   linewidth=3,
                   zorder=20)
                   
        ax.text(center[0], center[1] + 0.2, r'$z_0$', 
                ha='center', va='bottom', fontsize=label_fontsize, color=text_color, zorder=20)
        
        # --- レイアウト設定 ---
        # 4. キャプション（数式）を図の下に大きく表示
        ax.set_title(label, fontsize=math_fontsize, y=-0.2)

        # 軸の設定
        limit = 1.3
        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit, limit)
        ax.set_aspect('equal')
        ax.axis('off')

    # レイアウト調整
    plt.subplots_adjust(bottom=0.25)
    
    # 保存処理 (ディレクトリ自動生成付き)
    save_dir = "../src/chapters/img"
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, "fig_template_sample.pdf")
    
    plt.savefig(save_path, bbox_inches='tight')
    print(f"Saved sample figure to {save_path}")

if __name__ == "__main__":
    main()