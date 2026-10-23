import nflreadpy 
import polars as pl 


player_stats = nflreadpy.load_player_stats([2026])

# preparing receiver stats and team passing totals  

wide_receivers = player_stats.filter( 
    pl.col("position") == "WR"
)

receiver_stats = wide_receivers.select([
    "player_display_name",
    "week",
    "team",
    "targets",
    "receptions",
    "receiving_yards", 
    "receiving_tds"
])
# print(receiver_stats.head(5))

quarterbacks = player_stats.filter( 
    pl.col("position") == "QB"
)

# group QBs by team and week 
# sum QB passing attempts to estimate each team's weekly pass attempts 

quarterback_stats = quarterbacks.group_by([
    "week", 
    "team"
]).agg(
    pl.col("attempts").sum().alias("team_pass_attempts")
)

# Left join to attach each team's weekly passing attempts
# to its receivers while preserving all receiver records. 

receiver_opportunities = receiver_stats.join(
    quarterback_stats, 
    on=["team", "week"], 
    how="left"
)

# calculate and add column "target share"

receiver_opportunities = receiver_opportunities.with_columns(
    (pl.col("targets") / pl.col("team_pass_attempts")).alias("target_share")
)

# print(receiver_opportunities.head(5))
# print(receiver_opportunities.null_count())