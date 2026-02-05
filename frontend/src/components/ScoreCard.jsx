import { Card, CardContent, Typography } from "@mui/material";

const ScoreCard = ({ title, value }) => {
  return (
    <Card sx={{ minWidth: 200, textAlign: "center" }}>
      <CardContent>
        <Typography variant="h6">{title}</Typography>
        <Typography variant="h4" color="primary">
          {value}
        </Typography>
      </CardContent>
    </Card>
  );
};

export default ScoreCard;
